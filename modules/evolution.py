import dictionaries as d
import utils as u
from pprint import pprint
import numpy as np
from math import isnan


def top_average_column(data: dict, identifier: str, col: str, threshold: int) -> list:
    """
    - data: diccionari “net” que conté la informació de diversos sofifa_id
    - identifier: columna/clau que es fara servir com identificador
    - col: nom d’una columna/clau numérica
    - threshold: mínim número de dades necessàries
    """
    results = []
    for (key, value) in data.items():
        if threshold and not isnan(value[col][0]):
            mean_values = sum(value[col]) / len(value[col])
            results.append(
                (list(value[identifier])[0] if type(value[identifier]) == set else value[identifier], mean_values,
                 {'value': value[col], 'year': value['year']}))

    highest_numbers = sorted(results, key=lambda element: (element[1]))[-threshold:]
    return highest_numbers


if __name__ == "__main__":
    print("Evolution module")
    data = u.join_datasets_year("../data", [2016, 2017, 2018])
    columns_of_interest = ["short_name", "shooting", "gender", "year"]
    col_query = [("short_name", "one"), ("gender", "one")]
    data_dict = d.players_dict(data,
                               list(data["sofifa_id"].unique()),
                               columns_of_interest)
    data_dict = d.clean_up_players_dict(data_dict, col_query)
    pprint(top_average_column(data_dict, "short_name", "shooting", 4))
