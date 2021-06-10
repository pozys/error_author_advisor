import pandas as pd
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier

def trained_model(df):  
    df_normalized = preprocessing.normalize(df, axis=0)
    df_normalized_array = list(df_normalized)

    df_final = pd.DataFrame(df_normalized_array, columns=list(df.columns))
    
    X_train = df_final
    y_train = df.index
    clf = KNeighborsClassifier(n_neighbors=1)
    # clf = SVC()  
    clf.fit(X_train, y_train)

    return clf