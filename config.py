import os

class Config:
    COL_PREDICTION = "nutriscore_grade"
    MAX_ITERATIONS = 1000

    STATIC_DIRECTORY_PATH = "../static/"
    CSV_DIRECTORY_PATH = STATIC_DIRECTORY_PATH + "csv/"
    ORIGINAL_CSV_NAME = "en.openfoodfacts.org.products.csv"
    CLEANED_CSV_NAME = "openfoodfact_clean.csv"
    ORIGINAL_CSV_FULL_PATH = CSV_DIRECTORY_PATH + ORIGINAL_CSV_NAME
    CLEANED_CSV_FULL_PATH = CSV_DIRECTORY_PATH + CLEANED_CSV_NAME
    CHUNK_SIZE = 10000
    SELECTED_COLS = [
        "code",
        "product_name",
        "quantity",
        "brands",
        "categories",
        "ingredients_text",
        "nutriscore_score",
        "nutriscore_grade",
        "energy-kj_100g",
        "energy-kcal_100g",
        "fat_100g",
        "saturated-fat_100g",
        "omega-3-fat_100g",
        "omega-6-fat_100g",
        "sugars_100g",
        "added-sugars_100g",
        "fiber_100g",
        "proteins_100g",
        "salt_100g",
        "fruits-vegetables-nuts-estimate-from-ingredients_100g",
        "countries_en"
    ]
    COLS_STAT = [
        "nutriscore_score",
        "nutriscore_grade",
        "energy-kj_100g",
        "energy-kcal_100g",
        "fat_100g",
        "saturated-fat_100g",
        "omega-3-fat_100g",
        "omega-6-fat_100g",
        "sugars_100g",
        "added-sugars_100g",
        "fiber_100g",
        "proteins_100g",
        "salt_100g",
        "fruits-vegetables-nuts-estimate-from-ingredients_100g"
    ]
    COLS_100G = [
        "energy-kcal_100g",
        "fat_100g",
        "saturated-fat_100g",
        "sugars_100g",
        "fiber_100g",
        "proteins_100g",
        "salt_100g",
        "carbohydrates_100g",
        "nutriscore_grade",
    ]

    NUTRI_OK = ["a", "b", "c", "d", "e"]
    COUNTRIES_EN_COL = "countries_en"
    COUNTRIES_EN_API_URL = "https://restcountries.com/v3.1/all"
    UNKNOWN_STR = "Unknown"


    AVERAGE = 'weighted'
    SOLVER = "saga"
    DUMP_SCALER_PATH = 'models/scaler_nutriscore.pkl'
    DUMP_MODEL_PATH = 'models/model_nutriscore.pkl'
    DUMP_TEST_PATH = 'tests/df_test_nutriscore.pkl'