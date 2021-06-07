import pandas as pd
from sklearn import preprocessing
from sklearn.naive_bayes import MultinomialNB

def trained_model(df):  
    df_without_user = df.drop(columns='user')
    df_normalized = preprocessing.normalize(df_without_user, axis=0)
    df_normalized_array = list(df_normalized)

    df_final = pd.DataFrame(df_normalized_array, columns=df_without_user.columns)
    print(df_final.info())
    X = df_final
    y = df['user']
    
    clf = MultinomialNB()  
    clf.fit(X, y)

    return clf