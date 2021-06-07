import pandas as pd
import time

def get_test_dataframe(metadata: list, base_df):
    df_test = pd.DataFrame(columns=list(base_df.columns))

    df_test = df_test.append(pd.Series(dtype='float64'), ignore_index=True).fillna(0)    

    for item in metadata:
        df_test[item] = 1
    
    return df_test