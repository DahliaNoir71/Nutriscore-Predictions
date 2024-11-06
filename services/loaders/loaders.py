import os
import joblib

def load_model(model_name):
    """
    Load the trained model from the specified path.

    Parameters:
    model_name (str): The name of the model file.

    Returns:
    sklearn.base.BaseEstimator: The loaded trained model.
    """
    dump_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'dump', 'models')
    dump_model_path = os.path.join(dump_path, model_name)
    model = joblib.load(dump_model_path)
    return model


def load_scaler(scaler_name):
    """
    Load the scaler from the specified path.

    Parameters:
    scaler_name (str): The name of the scaler file.

    Returns:
    sklearn.preprocessing.Scaler: The loaded scaler.
    """
    dump_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'dump', 'models')
    dump_scaler_path = os.path.join(dump_path, scaler_name)
    scaler = joblib.load(dump_scaler_path)
    return scaler


def load_test_data(test_data_name):
    """
    Load the test data from the specified path.

    Parameters:
    test_data_name (str): The name of the test data file.

    Returns:
    pandas.DataFrame: The loaded test data.
    """
    dump_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'dump', 'tests')
    dump_test_path = os.path.join(dump_path, test_data_name)
    df_test = joblib.load(dump_test_path)
    return df_test