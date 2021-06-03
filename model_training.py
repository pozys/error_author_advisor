import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB

def trained_model(df):  
    df_without_user = df.drop(columns=['user'], level=0)
    df_normalized = preprocessing.normalize(df_without_user, axis=0)
    df_normalized_array = list(df_normalized)

    df_final = pd.DataFrame(df_normalized_array, columns=df_without_user.columns)
    
    X = df_final.drop(columns=['changed_data'], level=0)
    y = df['user']
    
    clf = MultinomialNB()  
    clf.fit(X, y)

    return clf