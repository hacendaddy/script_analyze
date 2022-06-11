"""This module calculates the BMI from FIFA Players."""
import pandas as pd
import matplotlib.pyplot as plt
from modules import utils


def calculate_bmi(data_frame: pd.DataFrame, gender: str, year: int,
                  cols_to_return: list) -> pd.DataFrame:
    """
    - df: dataframe que conté les dades
    - gender: gènere que volem estudiar
    - year: any que volem estudiar en format XXXX (per exemple 2020)
    - cols_to_return: llista de columnes que cal retornar (sense columna BMI)
    """
    temp = data_frame.loc[(data_frame['gender'] == gender)
                          & (data_frame['year'] == year)]
    temp['bmi'] = temp['weight_kg'] / (temp['height_cm'] / 100) ** 2
    cols_to_return.append('bmi')
    return temp[cols_to_return]


if __name__ == "__main__":
    print("This is BMI module.")
    DATA_FRAME = utils.join_datasets_year('../data', [2022])

    # Obtenim el bmi
    DATA = calculate_bmi(DATA_FRAME, 'M', 2022, ["sofifa_id", "club_flag_url"])

    # Mostrar una gràfica amb el BMI màxim per país
    PREP_DATA = DATA.groupby(DATA['club_flag_url'].str.slice(
        29, -4))['bmi'].max().reset_index()
    plt.bar(PREP_DATA["club_flag_url"], PREP_DATA["bmi"])
    plt.xticks(rotation=90)
    plt.show()
