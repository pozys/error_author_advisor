from datetime import date
import pandas as pd
import numpy as np
from sklearn import preprocessing
from pydantic.json import pydantic_encoder
import json
import os

def save_report(report):
    report_path = 'report.json'
    
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
    report_path = 'report.json'
    if not(os.path.exists(report_path) and os.path.getsize(report_path) > 0):
        return None
    
    report = pd.read_json(report_path)
   
    return report.iloc[-1]

def df_expanded(date = date.today()):
    df_orig = pd.read_json('report.json')

    df_orig = df_orig[df_orig['date'] <= pd.to_datetime(date)]

    if df_orig.size == 0:
        return None

    enc = preprocessing.OrdinalEncoder()
    df_orig['date'] = enc.fit_transform(df_orig[['date']])
    df_orig_normalized = preprocessing.normalize(df_orig[['date']], axis=0, norm='max')
    df_orig['date_coeff'] = df_orig_normalized
    df_orig['distance'] = 1 * df_orig['date_coeff']
    df_expanded = pd.pivot_table(df_orig, index=['user'], columns=['changed_data'], fill_value=0, aggfunc=np.sum). \
        reset_index()

    return df_expanded