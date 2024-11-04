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
    chunks = read_csv_chunks(file_path, selected_columns, chunk_size)
    # Concaténation des morceaux de DataFrame pour obtenir un DataFrame final
    df = pd.concat(chunks)
    return df

