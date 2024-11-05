def predictions(model, std_scaler, x_for_test):
    """
    Make predictions using a trained logistic regression model and a scaler.

    Parameters:
    log_reg_model (sklearn.linear_model.LogisticRegression): The trained logistic regression model.
    std_scaler (sklearn.preprocessing.StandardScaler): The scaler used to transform the input data.
    x_for_test (pd.DataFrame): A pandas DataFrame containing the features for the test set.

    Returns:
    y_prediction_test (pd.Series): A pandas Series containing the predicted target values for the test set.
    y_prediction_prob_test (np.ndarray): A numpy array containing the predicted probabilities for each class.
    """
    x_for_test = std_scaler.transform(x_for_test)
    y_prediction_test = model.predict(x_for_test)
    y_prediction_prob_test = model.predict_proba(x_for_test)
    return y_prediction_test, y_prediction_prob_test