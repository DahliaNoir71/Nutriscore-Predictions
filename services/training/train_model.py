import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from services.csv.csv import get_df_from_csv
from config import Config




def save_df_test(df_test):
    """
    Saves a DataFrame to a specified path using pickle.

    Parameters:
    df_test (pd.DataFrame): The DataFrame to be saved. This DataFrame should contain the test data.

    Returns:
    None: This function does not return any value. It saves the DataFrame to the specified path.

    The function constructs the dump path by joining the current file's directory,
    navigating up two levels, and then joining the 'static', 'dump', 'tests', and Config.DUMP_TEST_NAME directories.
    The path is normalized to avoid errors (e.g., with '..').
    The DataFrame is then saved to the constructed path using joblib's dump function.
    Finally, a success message is printed indicating that the DataFrame has been saved.
    """
    dump_path = os.path.join(os.path.dirname(__file__), '..', '..', 'static', 'dump', 'tests', Config.DUMP_TEST_NAME)
    # Normalize the path to avoid errors (e.g., with '..')
    dump_path = os.path.normpath(dump_path)
    with open(dump_path, 'wb') as file:
        pickle.dump(df_test, file)
    print("df_test sauvegardé avec succès.")


def split_data_for_test(df, test_size):
    """
    Splits a DataFrame into a training set and a test set.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the dataset. This DataFrame should contain all the columns
                        required for the prediction.
    test_size (float): The proportion of the dataset to include in the test split. The value should be between 0 and 1.
                        A value of 0.2 means that 20% of the data will be used for testing, and 80% will be used for training.

    Returns:
    pd.DataFrame: The modified DataFrame containing only the training data. The test data is saved to a separate CSV file.

    This function samples a specified proportion of the DataFrame as the test set. The remaining data is used as the training set.
    The test set is then saved to a separate CSV file using the save_df_test function. The modified DataFrame containing only the
    training data is returned.
    """
    print("Split data for test")
    df_test = df.sample(frac=test_size, random_state=1)  # Premier échantillon
    df = df.drop(df_test.index)  # Deuxième partie avec les lignes restantes
    save_df_test(df_test)
    return df


def preprocess_data(df, prediction_column):
    """
    Preprocess the dataset by splitting it into features (x) and target (y) variables.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing the dataset. This DataFrame should contain all the columns
                        required for the prediction, including the target variable.
    predictive_columns (str): The name of the column to be used as the target variable. This column should be present
                               in the input DataFrame.

    Returns:
    tuple: A tuple containing two pandas DataFrames. The first DataFrame (x) contains the features for the prediction,
           which are all columns in the input DataFrame except the target variable. The second DataFrame (y) contains
           the target variable.
    """
    print("Preprocess data")
    # Définir les features (x) et le target (y)
    # x contient toutes les colonnes sauf la colonne de prédiction
    # y contient la colonne de prédiction
    x = df.drop(prediction_column, axis=1)  # Features are all columns except the prediction column
    y = df[prediction_column]  # Target is the prediction column
    return x, y



def cross_validate_model(model, x, y, k=5, scoring='accuracy'):
    """
    Effectue une validation croisée sur le modèle spécifié.

    Paramètres :
    - model : le modèle ML à entraîner.
    - X : caractéristiques (features).
    - y : étiquettes (labels).
    - k : nombre de folds pour la cross-validation (par défaut 5).
    - scoring : métrique de scoring pour évaluer le modèle (par défaut 'accuracy').

    Retourne :
    - Un dictionnaire contenant les scores par fold, la moyenne des scores, et l’écart-type des scores.
    """
    print("Cross-validation")
    # Créer une instance du modèle
    # Utiliser verbose=1 pour afficher les informations de progression de l'entraînement
    # Utiliser cross_val_score pour effectuer la validation croisée
    # Utiliser 'accuracy' comme métrique de scoring pour évaluer le modèle
    # Effectuer la validation croisée
    scores = cross_val_score(model, x, y, cv=k, scoring=scoring)

    # Calculer les résultats
    cross_validation_results = {
        "scores": scores,
        "mean_score": np.mean(scores),
        "std_dev": np.std(scores)
    }

    # Afficher les résultats
    print("Scores de chaque fold :", cross_validation_results["scores"])
    print("Précision moyenne :", cross_validation_results["mean_score"])
    print("Écart-type des précisions :", cross_validation_results["std_dev"])

    return cross_validation_results


def train_model(x_for_train, y_for_train):
    """
    Train a logistic regression model using the provided training data.

    Parameters:
    x_train (pd.DataFrame): A pandas DataFrame containing the features for the training set.
                            The DataFrame should have the same number of columns as the features used in the model.
                            Each row represents a sample, and each column represents a feature.
    y_train (pd.Series): A pandas Series containing the target values for the training set.
                         The Series should have the same length as the number of samples in the training set.
                         Each element represents the target value for a corresponding sample.

    Returns:
    tuple: A tuple containing the trained logistic regression model and the fitted scaler.
           The model is an instance of the RandomForestClassifier class from the sklearn.ensemble module.
           The scaler is an instance of the StandardScaler class from the sklearn.preprocessing module.
           The scaler is used to standardize the features before training the model.
    """
    print("train model")
    std_scaler = StandardScaler()
    x_for_train = std_scaler.fit_transform(x_for_train)
    model = RandomForestClassifier(verbose=1)
    cross_validate_model(model, x_for_train, y_for_train)
    model.fit(x_for_train, y_for_train)
    return model, std_scaler

def save_model_and_scaler(model, scaler):
    """
    Saves the trained model and scaler to a specified directory.

    Parameters:
    model (sklearn.ensemble.RandomForestClassifier): The trained Random Forest model to be saved.
    scaler (sklearn.preprocessing.StandardScaler): The scaler used to standardize the input data.

    Returns:
    None: This function does not return any value. It saves the model and scaler to the specified directory.

    The function creates the 'trainings' directory if it does not already exist.
    Then, it saves the trained model and scaler to the 'trainings' directory using joblib's dump function.
    Finally, it prints a success message indicating that the model and scaler have been saved.
    """
    dump_path = os.path.join(os.path.dirname(__file__), 
                                   '..', 
                                   '..', 
                                   'static', 
                                   'dump', 
                                   'models')
    # Normalize the path to avoid errors (e.g., with '..')
    dump_path = os.path.normpath(dump_path)
    model_dump_path = os.path.join(dump_path, Config.DUMP_MODEL_NAME)
    scaler_dump_path = os.path.join(dump_path, Config.DUMP_SCALER_NAME)
    # Ensuite, sauvegarder le modèle et le scaler dans ce répertoire
    with open(model_dump_path, 'wb') as file:
        pickle.dump(model, file)
    with open(scaler_dump_path, 'wb') as file:
        pickle.dump(scaler, file)
    print("Modèle et scaler sauvegardés avec succès.")

def prepare_and_train_model():
    """
    Prepares and trains a machine learning model for predicting NutriScore.

    Parameters:
    saving (bool): A flag indicating whether to save the trained model and scaler.
                    If True, the model and scaler will be saved to the 'trainings' directory.

    Returns:
    tuple: A tuple containing the trained model, the scaler used for standardizing the input data,
           the features for the test set, and the target values for the test set.
           The model is an instance of the RandomForestClassifier class from the sklearn.ensemble module.
           The scaler is an instance of the StandardScaler class from the sklearn.preprocessing module.
           The features and target values for the test set are obtained using the train_test_split function
           from the sklearn.model_selection module.

    The function loads a cleaned CSV file containing data for predicting NutriScore.
    It then preprocesses the data by splitting it into features and target variables.
    The data is split into training and test sets using the train_test_split function.
    The function trains a Random Forest model using the training data.
    If the 'saving' parameter is True, the trained model and scaler are saved to the 'trainings' directory.
    Finally, the function returns the trained model, scaler, and the features and target values for the test set.
    """
    print("Prepare and train model")
    df_prediction = get_df_from_csv(Config.CLEANED_CSV_NAME,
                                    Config.COLS_PREDICTIONS,
                                    Config.CHUNK_SIZE)
    df_prediction = split_data_for_test(df_prediction,test_size=0.2)
    x, y = preprocess_data(df_prediction, Config.COL_PREDICTION)
    # feature_names = x.columns.tolist()  # Get the list of feature names from the DataFrame
    # print(feature_names)
    x_train, x_test, y_train, y_test = train_test_split(x,
                                                        y,
                                                        test_size=0.2,
                                                        random_state=42)
    model, scaler = train_model(x_train, y_train)
    save_model_and_scaler(model, scaler)

    return model, scaler, x_test, y_test



