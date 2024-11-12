import os
import pickle

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
    with open(dump_model_path, 'rb') as file:
        model = pickle.load(file)
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
    with open(dump_scaler_path, 'rb') as file:
        scaler = pickle.load(file)
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
    with open(dump_test_path, 'rb') as file:
        df_test = pickle.load(file)
    return df_test