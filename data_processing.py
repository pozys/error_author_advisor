import pandas as pd

def get_test_dataframe(metadata: str, base_df):
    df_test = pd.DataFrame(columns=base_df.columns)
    df_test = df_test.append(pd.Series(dtype='float64'), ignore_index=True).fillna(0)

    # module = 'РегистрСведений.КартинкиИФайлы.Форма.ФормаЗаписи'
    df_test['distance', metadata] = 1
    
    df_test = df_test.drop(columns=['user', 'changed_data'], level=0)

    return df_test