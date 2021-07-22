import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def trained_model(df):
    df_final = pd.DataFrame(df, columns=list(df.columns))
    X_train = df_final
    y_train = df.index
    feature_count = len(df_final.columns) 
    clf = KNeighborsClassifier(n_neighbors=1)
    clf.fit(X_train, y_train)

    return clf