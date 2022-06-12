"""This module creates dictionaries and cleans them."""
import re
import pandas as pd


def players_dict(data_frame: pd.DataFrame, ids: list, cols: list) -> dict:
    """
    - df: dataframe que conté les dades
    - ids: llista d’iidentificador “sofifa_id”
    - cols: llista de columnes de les que volem informació
    """
    cols.append('sofifa_id')
    temp = data_frame[cols]
    temp.set_index('sofifa_id', inplace=True)
    temp = temp.groupby('sofifa_id').agg(lambda x: x.values.tolist()).T.to_dict()
    temp = dict((k, temp[k]) for k in ids if k in temp)
    cols.pop()

    return temp


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
