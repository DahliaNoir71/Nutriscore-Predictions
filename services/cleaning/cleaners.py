from config import Config

def clean_nutriscore(df, selected_column):
    """
    Cleans a DataFrame by removing rows with missing values in the specified column and filtering the DataFrame to keep only rows
    where the selected column contains one of the specified values.

    Parameters:
    df (pandas.DataFrame): The DataFrame to clean.
    selected_column (str): The name of the column to clean.

    Returns:
    pandas.DataFrame: The cleaned DataFrame.
    """
    print("Début clean nutriscore")
    df = df.dropna(subset=[selected_column])
    # Normalisation de la colonne avant comparaison
    df[selected_column] = df[selected_column].str.lower()
    df[selected_column] = df[selected_column].str.strip()
    # Filter the DataFrame to keep only rows where the 'nutriscore_grade' column contains one of the specified values
    df = df[df[selected_column].isin(Config.NUTRI_OK)]
    print("Fin clean nutriscore")
    return df


def clean_by_country(df, column_name, country_name):
    """
    Cleans a DataFrame by splitting a column containing multiple countries into separate rows,
    cleaning the resulting values, and filtering the DataFrame to keep only rows where the column contains a specific country.

    Parameters:
    df (pandas.DataFrame): The DataFrame to clean.
    column_name (str): The name of the column containing the countries.
    country_name (str): The name of the country to filter for.

    Returns:
    pandas.DataFrame: The cleaned DataFrame, containing only rows where the specified column contains the specified country.
    """
    print("Début clean by country")
    # Divide and explode to obtain each country as a separate row
    df[column_name] = df[column_name].str.split(',')
    df = df.explode(column_name)
    # Clean extra spaces and normalize to lowercase
    df[column_name] = df[column_name].str.strip()
    df[column_name] = df[column_name].str.lower()
    # Filter the dataframe to keep only rows where the column contains the word country_name
    df = df[df[column_name].str.contains(country_name.lower(), na=False)]
    print("Fin clean by country")
    return df