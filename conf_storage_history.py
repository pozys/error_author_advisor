# #!/usr/bin/env python
# # coding: utf-8

# # In[1]:


# import pandas as pd
# import math
# import matplotlib.pyplot as plt
# import seaborn as sns
# import numpy as np
# from sklearn.model_selection import GridSearchCV
# get_ipython().run_line_magic('matplotlib', 'inline')
# from IPython.display import SVG
# from graphviz import Source
# from IPython.display import display
# from sklearn.model_selection import train_test_split
# from sklearn import preprocessing
# from sklearn.naive_bayes import MultinomialNB
# import functools

# @functools.lru_cache(maxsize=50)
# def df_expanded():
#     df_orig = pd.read_json('G:/Документы/Работа/data.json')

#     enc = preprocessing.OrdinalEncoder()
#     df_orig['date'] = enc.fit_transform(df_orig[['date']])

#     df_orig_normalized = preprocessing.normalize(df_orig[['date']], axis=0, norm='max')
#     df_orig['date_coeff'] = df_orig_normalized
#     df_orig['distance'] = 1 * df_orig['date_coeff']

#     df_expanded = pd.pivot_table(df_orig, index=['user'], columns=['changed_data'], fill_value=0, aggfunc=np.sum).         reset_index() #, values=['distance']
    
#     return df_expanded

# df_expanded = df_expanded()


# # In[2]:


# users = df_expanded['user']
# df_without_user = df_expanded.drop(columns=['user'], level=0)
# df_normalized = preprocessing.normalize(df_without_user, axis=0)
# df_normalized_array = list(df_normalized)

# df_final = pd.DataFrame(df_normalized_array, columns=df_without_user.columns)
# df_final['user'] = list(users)


# # In[3]:



# df_test = pd.DataFrame(columns=df_final.columns)
# df_test = df_test.append(pd.Series(dtype='float64'), ignore_index=True).fillna(0)

# module = 'РегистрСведений.КартинкиИФайлы.Форма.ФормаЗаписи'
# df_test['distance', module] = 1
# # df_test['distance', 'ОбщийМодуль.фзФоновыеЗадания'] = 1
# df_test = df_test.drop(columns=['user', 'changed_data'], level=0)

# X = df_final.drop(columns=['user', 'changed_data'], level=0)
# y = df_final['user']

# clf = MultinomialNB()
# clf.fit(X, y)

# prediction = clf.predict(df_test)
# name = prediction[0]
# print(name)
# df_final_t = df_final[df_final['user'] == name]
# print(df_final_t[[('distance', module)]])
# print(df_final_t[[('distance', module)]].max())

# # df_final[['user']]
# # df_final.info()


# # In[4]:


# # df = pd.read_excel('G:\Документы\Работа\conf_storage_history_full.xlsx', index_col='date', parse_dates=True)

