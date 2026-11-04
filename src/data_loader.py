import pandas as pd

class DataLoadError(Exception):
    """Error during the import of experimental data."""
    pass

def load_data(file):
    """
    Import experimental data exported by the catman software.

    Accepts a file path or a file-like object.

    Raises:
        DataLoadError: If the file uses the American decimal pattern (.) 
                       instead of the expected Brazilian pattern (,).
    """

    # Read the Excel file
    try:
        planilha = pd.read_excel(file, header=None, decimal=",")
    except Exception as erro:
        raise DataLoadError(f"Could not read the file: {erro}")

    # Check if the DataFrame is empty
    if planilha.empty:
        raise DataLoadError("The imported file is empty.")

    # Identify the first row with numerical data
    dados_numericos = planilha.apply(pd.to_numeric, errors="coerce")
    linhas_validas = dados_numericos.notna().all(axis=1)
    indices = linhas_validas[linhas_validas].index

    if len(indices) == 0:
        raise DataLoadError("No experimental data found.")
    
    inicio = indices[0]

    # Extract experimental data starting from the first valid row
    dados = dados_numericos.iloc[inicio:].copy()

    # remove rows with any NaN values
    dados = dados.dropna(how="any")

    # Extract original header
    metadados = planilha.iloc[:inicio].copy()

    # Reset indexes
    dados = dados.reset_index(drop=True)
    metadados = metadados.reset_index(drop=True)

    return dados, metadados