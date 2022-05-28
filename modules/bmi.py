import pandas as pd
import utils
import matplotlib.pyplot as plt


def calculate_BMI(df: pd.DataFrame, gender: str, year: int, cols_to_return: list) -> pd.DataFrame:
    '''
    - df: dataframe que conté les dades
    - gender: gènere que volem estudiar
    - year: any que volem estudiar en format XXXX (per exemple 2020)
    - cols_to_return: llista de columnes que cal retornar (sense columna BMI)
    '''
    temp = df.loc[(df['gender'] == gender) & (df['year'] == year)]
    temp['bmi'] = temp['weight_kg'] / (temp['height_cm']/100) ** 2
    cols_to_return.append('bmi')
    return temp[cols_to_return]


if __name__ == "__main__":
    print("This is BMI module.")
    df = utils.join_datasets_year('data/', [2022])
    data = calculate_BMI(df, 'M', 2022, ["sofifa_id", "club_flag_url"])
    var = data['club_flag_url'].str.slice(29, -4)
    var.value_counts().plot(kind='bar')
    plt.show()

    # https: // cdn.sofifa.net/flags/fr.png
