
def error_author_prediction(model, df_test):
    prediction = model.predict(df_test)
    name = prediction[0]
    
    return name