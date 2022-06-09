from pprint import pprint
from modules import utils

import pandas as pd


def players_dict(df: pd.DataFrame, ids: list, cols: list) -> dict:
    """
    - df: dataframe que conté les dades
    - ids: llista d’iidentificador “sofifa_id”
    - cols: llista de columnes de les que volem informació
    """
    cols.append('sofifa_id')
    temp = df[cols]
    temp.set_index('sofifa_id', inplace=True)
    temp = temp.groupby('sofifa_id').agg(lambda x: x.values.tolist()).T
    temp_dict = temp.to_dict()
    result = dict((k, temp_dict[k]) for k in ids if k in temp_dict)
    return result


def clean_up_players_dict(player_dict: dict, col_query: list) -> dict:
    """
    - player_dict: diccionari amb el formato de l’apartat (a) players_dict
    - col_query: llista de tuples amb detalls sobre la información que cal simplificar
    """
    # TODO:: Fix repetitions
    """res = dict()
    for (key, value) in player_dict.items():
        for element in col_query:
            value[element[0]] = set(value[element[0]])

        res[key] = value

    return res"""

    res = dict()
    for ident, params in player_dict.items():
        params[col_query[0][0]] = set(params[col_query[0][0]])
        params[col_query[1][0]] = params[col_query[1][0]][:1]
        res[ident] = params
    return res


if __name__ == "__main__":
    print("Dictionaries module")
    df = utils.join_datasets_year('../data', [2016, 2017, 2018])
    test_dict = players_dict(df, [226328, 192476, 230566],
                             ["short_name", "overall", "potential", "player_positions", "year"])
    col_query = [("short_name", "del_rep"), ('potential', 'one')]
    pprint(clean_up_players_dict(test_dict, col_query))
