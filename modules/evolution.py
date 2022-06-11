"""This module calculates the mean of a column."""
from pprint import pprint
from math import isnan
from modules import dictionaries, utils


def top_average_column(data: dict, identifier: str, col: str, threshold: int) -> list:
    """
    - data: diccionari “net” que conté la informació de diversos sofifa_id
    - identifier: columna/clau que es fara servir com identificador
    - col: nom d’una columna/clau numérica
    - threshold: mínim número de dades necessàries
    """
    results = []
    for (_, value) in data.items():
        if threshold and not isnan(value[col][0]):
            mean_values = sum(value[col]) / len(value[col])
            results.append(
                (list(value[identifier])[0] if isinstance(value[identifier]) == set
                 else value[identifier], mean_values,
                 {'value': value[col], 'year': value['year']}))

    highest_numbers = sorted(
        results, key=lambda element: (element[1]))[-threshold:]
    return highest_numbers


if __name__ == "__main__":
    print("Evolution module")
    DATA_FRAME = utils.join_datasets_year("../data", [2016, 2017, 2018])
    COLUMNS_OF_INTEREST = ["short_name", "shooting", "gender", "year"]
    COL_QUERY = [("short_name", "one"), ("gender", "one")]
    DATA_DICT = dictionaries.players_dict(DATA_FRAME,
                                          list(
                                              DATA_FRAME["sofifa_id"].unique()),
                                          COLUMNS_OF_INTEREST)
    DATA_DICT = dictionaries.clean_up_players_dict(DATA_DICT, COL_QUERY)
    pprint(top_average_column(DATA_DICT, "short_name", "shooting", 4))
