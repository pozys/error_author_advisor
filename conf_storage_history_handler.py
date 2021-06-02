import pandas as pd
import numpy as np
from sklearn import preprocessing
from pydantic.json import pydantic_encoder
import json

def save_report(report):
    file = open('report.json', 'w')
    report_to_json = json.dumps(report, default=pydantic_encoder)
    # print(report)
    file.write(report_to_json)
    file.close()

def df_expanded():
    df_orig = pd.read_json('report.json')

    enc = preprocessing.OrdinalEncoder()
    df_orig['date'] = enc.fit_transform(df_orig[['date']])
    df_orig_normalized = preprocessing.normalize(df_orig[['date']], axis=0, norm='max')
    df_orig['date_coeff'] = df_orig_normalized
    df_orig['distance'] = 1 * df_orig['date_coeff']
    df_expanded = pd.pivot_table(df_orig, index=['user'], columns=['changed_data'], fill_value=0, aggfunc=np.sum). \
        reset_index() #, values=['distance']

    return df_expanded.head()