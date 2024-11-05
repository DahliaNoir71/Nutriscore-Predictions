from app.services.cleaning.cleaners import clean_nutriscore, clean_by_country
from app.services.csv.csv import get_df_from_csv
from app.config import Config

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
    df_to_clean = get_df_from_csv(Config.ORIGINAL_CSV_FULL_PATH,
                                  Config.COLS_TO_CLEAN,
                                  Config.CHUNK_SIZE)
    df_cleaned = clean_nutriscore(df_to_clean, Config.COL_PREDICTION)
    df_cleaned = clean_by_country(df_cleaned,
                                  Config.COL_COUNTRIES_EN,
                                  Config.COUNTRY_TO_CLEAN)
    df_cleaned = df_cleaned.drop(Config.COL_COUNTRIES_EN, axis=1)
    # Save the cleaned DataFrame to a new CSV file with tab-separated values and without the index column
    df_cleaned.to_csv(Config.CLEANED_CSV_FULL_PATH, sep='\t', index=False)
    print("CSV sauvegardé")
    print("Fin de script clean_csv")

# Call the main function
if __name__ == "__main__":
    main()