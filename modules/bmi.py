"""This module calculates the BMI from FIFA Players."""
import pandas as pd


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
    temp['BMI'] = temp['weight_kg'] / (temp['height_cm'] / 100) ** 2
    cols_to_return.append('BMI')
    return temp[cols_to_return]


if __name__ == "__main__":
    print("This is BMI module.")
