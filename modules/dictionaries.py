"""This module creates dictionaries and cleans them."""
from pprint import pprint
import re
import pandas as pd
from modules import utils


def players_dict(data_frame: pd.DataFrame, ids: list, cols: list) -> dict:
    """
    - df: dataframe que conté les dades
    - ids: llista d’iidentificador “sofifa_id”
    - cols: llista de columnes de les que volem informació
    """
    cols.append('sofifa_id')
    temp = data_frame[cols]
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
    res = dict()

    for key, value in player_dict.items():
        for element in col_query:
            if element[1] == "del_rep":
                seen = []
                for i in value[element[0]]:
                    i = re.sub(r'[\s+]', '', i)
                    i = i.split(",")
                    for j in i:
                        if j not in seen:
                            seen.append(j)
                value[element[0]] = set(seen)
            elif element[1] == "one":
                value[element[0]] = value[element[0]][0]
        res[key] = value
    return res


if __name__ == "__main__":
    print("Dictionaries module")
    DATA_FRAME = utils.join_datasets_year('../data', [2016, 2017, 2018])
    TEST_DICT = players_dict(DATA_FRAME, [226328, 192476, 230566],
                             ["short_name", "overall", "potential", "player_positions", "year"])

    COL_QUERY = [("short_name", "del_rep"), ('potential', 'one')]
    pprint(clean_up_players_dict(TEST_DICT, COL_QUERY))
