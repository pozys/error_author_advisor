import pandas as pd
import time

def get_test_dataframe(metadata: list, base_df):
    t0 = time.time()
    df_test = pd.DataFrame(columns=base_df.columns)
    t1 = time.time() - t0
    print("Time elapsed on 1: ", t1)
    
    t0 = time.time()
    df_test = df_test.append(pd.Series(dtype='float64'), ignore_index=True).fillna(0)
    t1 = time.time() - t0
    print("Time elapsed on 2: ", t1)
    

    t0 = time.time()
    for item in metadata:
        df_test['distance', item] = 1
    t1 = time.time() - t0
    print("Time elapsed on 3: ", t1)
    
    t0 = time.time()
    df_test = df_test.drop(columns=['user', 'changed_data'], level=0)
    t1 = time.time() - t0
    print("Time elapsed on 4: ", t1)
    

    return df_test