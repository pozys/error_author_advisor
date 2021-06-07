from datetime import date
import pandas as pd
import numpy as np
from sklearn import preprocessing
from pydantic.json import pydantic_encoder
import json
import os

report_path = 'report.json'

def save_report(report):
    if not(os.path.exists(report_path) and os.path.getsize(report_path) > 0):
        existing_report = []
        file = open(report_path, 'w+')
    else:
        file = open(report_path, 'r+')
        existing_report = json.load(file)
    
    for report_item in report:
        existing_report.append(report_item)

    report_to_json = json.dumps(existing_report, default=pydantic_encoder)
    file.seek(0)
    file.truncate()
    file.write(report_to_json)
    file.close()

def get_last_storage_version():    
    if not(os.path.exists(report_path) and os.path.getsize(report_path) > 0):
        return None
    
    report = pd.read_json(report_path)
   
    return report.iloc[-1]

def df_expanded(date = date.today()):
    df_report = df_raw_report()

    df_report = df_report[df_report['date'] <= pd.to_datetime(date)]

    if df_report.size == 0:
        return None

    enc = preprocessing.OrdinalEncoder()
    df_report['date'] = enc.fit_transform(df_report[['date']])
    df_report_normalized = preprocessing.normalize(df_report[['date']], axis=0, norm='max')
    df_report['date_coeff'] = df_report_normalized
    df_report['distance'] = 1 * df_report['date_coeff']
    df_expanded = pd.pivot_table(df_report, index=['user'], columns=['changed_data'], fill_value=0, aggfunc=np.sum). \
        reset_index()

    return df_expanded

def df_raw_report():
    return pd.read_json(report_path)