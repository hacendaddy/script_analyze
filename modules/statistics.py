import pandas as pd


def find_max_col(df: pd.DataFrame, filter_col: str, cols_to_return: list) -> pd.DataFrame:
    '''
    - df: dataframe que conté les dades
    - filter_col: nom de la columna de la que volem saber el màxim
    - cols_to_return: llista de columnes que cal retornar
    '''
    max_value = df.loc[df[filter_col].idxmax()]
    return max_value[cols_to_return]


def find_rows_query(df: pd.DataFrame, query: tuple, cols_to_return: list) -> pd.DataFrame:
    '''
    - df: dataframe que conté les dades
    - query: tupla que conté la query
    - cols_to_return: llista de columnes que cal retornar
    '''
    '''print(query[0][0], "==", query[1][0])
    print(query[0][1], "==", query[1][1][0])
    print(query[0][1], "==", query[1][1][1])'''

    # TODO:: Finish this


if __name__ == "__main__":
    print("This is statistics module")
    df = pd.read_csv('data/players_20.csv')
    cols_to_return = ["sofifa_id", "player_url", "short_name", "long_name"]
    '''
    filter_col = "weight_kg"
    find_max_col(df, filter_col, cols_to_return)
    '''
    # Under construction
    # 1a, 2a - 1b, 2b
    query = (["league_name", "weight_kg"], [
        "English Premier League", (60, 70)])
    find_rows_query(df, query, cols_to_return)
