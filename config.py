import os

class Config:
    MAX_ITERATIONS = 1000
    STATIC_DIRECTORY_PATH = "../static/"
    CSV_DIRECTORY_PATH = STATIC_DIRECTORY_PATH + "csv/"
    ORIGINAL_CSV_NAME = "en.openfoodfacts.org.products.csv"
    CLEANED_CSV_NAME = "openfoodfact_clean.csv"
    ORIGINAL_CSV_FULL_PATH = CSV_DIRECTORY_PATH + ORIGINAL_CSV_NAME
    CLEANED_CSV_FULL_PATH = CSV_DIRECTORY_PATH + CLEANED_CSV_NAME
    CHUNK_SIZE = 10000
    COL_PREDICTION = "nutriscore_grade"
    COL_COUNTRIES_EN = "countries_en"
    COLS_100G = [
        "energy-kcal_100g",
        "fat_100g",
        "saturated-fat_100g",
        "sugars_100g",
        "fiber_100g",
        "proteins_100g",
        "salt_100g",
        "fruits-vegetables-nuts-estimate-from-ingredients_100g"
    ]
    COLS_PREDICTIONS = COLS_100G + [COL_PREDICTION]
    COLS_TO_CLEAN = COLS_PREDICTIONS + [COL_COUNTRIES_EN]
    DUMP_SCALER_NAME = 'scaler_nutriscore.pkl'
    DUMP_MODEL_NAME = 'model_nutriscore.pkl'
    DUMP_TEST_NAME = 'df_test_nutriscore.pkl'
    NUTRI_OK = ["a", "b", "c", "d", "e"]
    COUNTRY_TO_CLEAN = "France"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskuser:flaskpassword@mysql-db/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False




