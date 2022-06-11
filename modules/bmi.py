import pandas as pd
from modules import utils
import matplotlib.pyplot as plt


def calculate_bmi(df: pd.DataFrame, gender: str, year: int, cols_to_return: list) -> pd.DataFrame:
    """
    - df: dataframe que conté les dades
    - gender: gènere que volem estudiar
    - year: any que volem estudiar en format XXXX (per exemple 2020)
    - cols_to_return: llista de columnes que cal retornar (sense columna BMI)
    """
    temp = df.loc[(df['gender'] == gender) & (df['year'] == year)]
    temp['bmi'] = temp['weight_kg'] / (temp['height_cm'] / 100) ** 2
    cols_to_return.append('bmi')
    return temp[cols_to_return]


if __name__ == "__main__":
    print("This is BMI module.")
    df = utils.join_datasets_year('../data', [2022])

    # Obtenim el bmi
    data = calculate_bmi(df, 'M', 2022, ["sofifa_id", "club_flag_url"])

    # Mostrar una gràfica amb el BMI màxim per país
    prep_data = data.groupby(data['club_flag_url'].str.slice(29, -4))['bmi'].max().reset_index()
    plt.bar(prep_data["club_flag_url"], prep_data["bmi"])
    plt.xticks(rotation=90)
    plt.show()
