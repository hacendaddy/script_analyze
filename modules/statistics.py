"""This module finds cols based on conditions."""
import pandas as pd
import numpy as np


def find_max_col(data_frame: pd.DataFrame, filter_col: str,
                 cols_to_return: list) -> pd.DataFrame:
    """
    - df: dataframe que conté les dades
    - filter_col: nom de la columna de la que volem saber el màxim
    - cols_to_return: llista de columnes que cal retornar
    """
    max_value = data_frame.loc[data_frame[filter_col].idxmax()]
    return max_value[cols_to_return]


def find_rows_query(data_frame: pd.DataFrame, query: tuple,
                    cols_to_return: list) -> pd.DataFrame:
    """
    - df: dataframe que conté les dades
    - query: tupla que conté la query
    - cols_to_return: llista de columnes que cal retornar
    """
    # Columnes numèriques
    numeric_columns = data_frame.select_dtypes(include=[np.number])

    # Preview de la query
    # (["league_name", "weight_kg"], ["English Premier League", (60, 70)])

    # Transformació a objecte [(key, value), (key, value)]
    new_object = list(zip(query[0], query[1]))

    # Loop principal assignació i filtratge
    for (col, val) in new_object:
        # Si la columna es numérica
        if col in numeric_columns:
            # No fem servir type per el pylint
            data_frame = data_frame[data_frame[col].between(val[0], val[1])]
        else:
            data_frame = data_frame[data_frame[col] == val]

    return data_frame[cols_to_return]


if __name__ == "__main__":
    print("This is statistics module")
