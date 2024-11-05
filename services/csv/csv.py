import pandas as pd
from tqdm import tqdm


def read_csv_chunks(file_path, selected_columns, chunk_size):
    """
    Read a CSV file in chunks and return a list of DataFrame chunks.

    :param file_path: The path to the CSV file to be read.
    :param selected_columns: A list of column names to be read from the CSV file.
    :param chunk_size: The number of rows per chunk to be read from the CSV file.
    :return: A list of DataFrame chunks, each containing the selected columns from the CSV file.
    """
    # Initialisation de la liste pour stocker les morceaux sélectionnés
    selected_chunks = []

    # Lire le fichier CSV en chunks avec une barre de progression
    if selected_columns:
        chunk_iter = pd.read_csv(file_path,
                                sep="\t",
                                low_memory=False,
                                header=0,
                                chunksize=chunk_size,
                                on_bad_lines="skip",
                                usecols=selected_columns)
    else:
        chunk_iter = pd.read_csv(file_path,
                                sep="\t",
                                low_memory=False,
                                header=0,
                                chunksize=chunk_size,
                                on_bad_lines="skip")

    with tqdm(desc="Lecture du CSV " + file_path, unit='chunk') as pbar:
        for chunk in chunk_iter:
            selected_chunks.append(chunk)
            # Mise à jour de la barre de progression
            pbar.update(1)
            # (Optionnel) Afficher des informations supplémentaires dans la barre de progression
            pbar.set_postfix(rows=chunk.shape[0])

    return selected_chunks

def get_df_from_csv(file_path, selected_columns, chunk_size):
    """
    Load a CSV file into a pandas DataFrame, either by loading a previously saved DataFrame or by reading the CSV file in chunks.

    Parameters:
    file_path (str): The path to the CSV file to be loaded.
    selected_columns (list): A list of column names to be read from the CSV file. If None, all columns will be read.
    chunk_size (int): The number of rows per chunk to be read from the CSV file.
    debug (bool): A flag indicating whether debug mode is enabled.

    Returns:
    pd.DataFrame: The loaded DataFrame containing the CSV data. If debug mode is enabled, the DataFrame will be saved to a file for future use.
    """
    chunks = read_csv_chunks(file_path, selected_columns, chunk_size)
    # Concatenate the chunks of DataFrame to obtain a final DataFrame
    df = pd.concat(chunks)

    return df