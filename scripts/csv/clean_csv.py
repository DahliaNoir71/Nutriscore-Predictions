from services.cleaning.cleaners import clean_nutriscore, clean_by_country
from services.csv.csv import get_df_from_csv, save_cleaned_csv
from config import Config

def main():
    """
    This function is responsible for cleaning the original CSV file and saving the cleaned data to a new CSV file.

    Parameters:
    -----------
    None

    Returns:
    --------
    None
    """
    print("Début de script clean_csv")
    df_to_clean = get_df_from_csv(Config.ORIGINAL_CSV_NAME,
                                  Config.COLS_TO_CLEAN,
                                  Config.CHUNK_SIZE)
    df_cleaned = clean_nutriscore(df_to_clean, Config.COL_PREDICTION)
    df_cleaned = clean_by_country(df_cleaned,
                                  Config.COL_COUNTRIES_EN,
                                  Config.COUNTRY_TO_CLEAN)
    df_cleaned = df_cleaned.drop(Config.COL_COUNTRIES_EN, axis=1)
    # Save the cleaned DataFrame to a new CSV file with tab-separated values and without the index column
    save_cleaned_csv(df_cleaned, Config.CLEANED_CSV_NAME)
    print("Fin de script clean_csv")

# Call the main function
if __name__ == "__main__":
    main()