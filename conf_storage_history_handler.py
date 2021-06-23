from datetime import date
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sqlalchemy.orm import Session
from sqlalchemy import desc
from functools import lru_cache

import models
from database import engine

def save_report(report, db: Session):
    new_items = []

    for item in report:
        history_item = models.History(
            version=item.version, 
            date=item.date, 
            user=item.user, 
            changed_data=item.changed_data
            )

        new_items.append(history_item)

    if not new_items:
        return
        
    db.add_all(new_items)
    db.commit()

    df_raw_report.cache_clear()

def get_last_storage_version(db: Session):
    result = db.query(models.History).order_by(desc(models.History.version)).first()
    
    return result       

def df_expanded(metadata: list = [], date = date.today()):
    df_report = df_raw_report()
    df_report = df_report[df_report['date'] <= pd.to_datetime(date)]
    
    if metadata:
        metadata_unique = set(metadata)
        df_report = df_report[df_report['changed_data'].isin(metadata_unique)]
        df_report['metadata_index'] = df_report['changed_data']. \
            apply(lambda item : len(metadata) - 1 - metadata[::-1].index(item))
    else:
        df_report = df_report.copy()
        df_report['metadata_index'] = 1

    if df_report.size == 0:
        return None

    df_report = df_report.drop(columns=['id'])

    scaler = MinMaxScaler(feature_range=(0.0000001, 1))
    
    df_report['date_coeff'] = scaler.fit_transform(df_report[['date']])
    df_report['metadata_coeff'] = scaler.fit_transform(df_report[['metadata_index']])
    df_report['distance'] = 1 * df_report['date_coeff'] * df_report['metadata_coeff']
    df_expanded = pd.pivot_table(df_report, index='user', values='distance', columns='changed_data', fill_value=0, aggfunc=np.sum). \
        reset_index()
    df_expanded = df_expanded.set_index('user')
    df_expanded = pd.DataFrame(scaler.fit_transform(df_expanded), index=df_expanded.index, columns=list(df_expanded.columns))

    return df_expanded

@lru_cache
def df_raw_report():
    df_report = pd.read_sql_table(models.History.__tablename__, engine)
    
    return df_report