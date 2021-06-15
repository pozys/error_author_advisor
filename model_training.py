import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler

def trained_model(df):  
    scaler = MinMaxScaler()
    df_final = pd.DataFrame(scaler.fit_transform(df), columns=list(df.columns))
    
    X_train = df_final
    y_train = df.index
    feature_count = len(df_final.columns) 
    clf = KNeighborsClassifier(n_neighbors=feature_count)
    clf.fit(X_train, y_train)

    return clf