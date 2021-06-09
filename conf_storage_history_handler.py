from datetime import date
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sqlalchemy.orm import Session
from sqlalchemy import desc

import models, schemas
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

def get_last_storage_version(db: Session):
    result = db.query(models.History).order_by(desc(models.History.version)).first()
    
    return result       

def df_expanded(metadata, date = date.today()):
    df_report = df_raw_report()
    df_report = df_report[df_report['date'] <= pd.to_datetime(date)]
    
    if metadata:
        df_report = df_report[df_report['changed_data'].isin(metadata)]

    if df_report.size == 0:
        return None

    df_report = df_report.drop(columns=['id'])
    enc = preprocessing.OrdinalEncoder()
    
    df_report['date']  = df_report['date'].dt.date
    df_report['date'] = enc.fit_transform(df_report[['date']])
    df_report_normalized = preprocessing.normalize(df_report[['date']], axis=0, norm='max')
    df_report['date_coeff'] = df_report_normalized
    df_report['distance'] = 1 * df_report['date_coeff']
    df_expanded = pd.pivot_table(df_report, index='user', values='distance', columns='changed_data', fill_value=0, aggfunc=np.sum). \
        reset_index()
    df_expanded = df_expanded.set_index('user')

    return df_expanded

def df_raw_report():
    df_report = pd.read_sql_table(models.History.__tablename__, engine)

    return df_report