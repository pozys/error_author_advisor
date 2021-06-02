import pandas as pd
import numpy as np
from sklearn import preprocessing

def df_expanded():
    df_orig = pd.read_excel('G:\Документы\Работа\conf_storage_history_full.xlsx', parse_dates=['date'])

    enc = preprocessing.OrdinalEncoder()
    df_orig['date'] = enc.fit_transform(df_orig[['date']])
    df_orig_normalized = preprocessing.normalize(df_orig[['date']], axis=0, norm='max')
    df_orig['date_coeff'] = df_orig_normalized
    df_orig['distance'] = 1 * df_orig['date_coeff']
    df_expanded = pd.pivot_table(df_orig, index=['user'], columns=['changed_data'], fill_value=0, aggfunc=np.sum). \
        reset_index() #, values=['distance']

    return df_expanded