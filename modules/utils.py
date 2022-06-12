"""This module merges csvs and adds columns."""
import glob
import datetime
import os
import pandas as pd


def get_small_year(full_year: int) -> str:
    """
    Transforms a full given year XXXX to a small one XX
    - full_year: year as number
    """
    # Transform to a date
    temp_d = datetime.date(full_year, 1, 1)

    # Get the date
    return temp_d.strftime("%y")


def read_add_year_gender(filepath: str, gender: str, year: int) -> pd.DataFrame:
    """
    - filepath: string amb la ruta de l’arxiu que volem llegir
    - gender: 'M' o 'F' (segons les sigles de “Male” or “Female”)
    - year: Any al que corresponen les dades en format XXXX (per exemple, 2020)
    """
    data_frame = pd.read_csv(filepath, low_memory=False)
    data_frame['gender'] = gender
    data_frame['year'] = year
    return data_frame


def join_male_female(path: str, year: int) -> pd.DataFrame:
    """
    - path: ruta a la carpeta que conté les dades
    - year: any del que es volen llegir les dades, format XXXX (per exemple, 2020)
    """
    new_path = os.path.join(f"{path}", f'*{get_small_year(year)}.csv')

    all_filenames = [i for i in glob.glob(new_path)]
    csvs = []
    for i in all_filenames:
        gender = 'M' if 'female' not in i else 'F'
        temp = read_add_year_gender(i, gender, year)
        csvs.append(temp)

    return pd.concat(csvs)


def join_datasets_year(path: str, years: list) -> pd.DataFrame:
    """
    - path: ruta a la carpeta que conté les dades
    - years: llista d’anys que es volen incloure en el dataframe, en format [XXXX,...]
    """
    csvs = []

    for year in years:
        gender = join_male_female(path, year)
        csvs.append(gender)

    return pd.concat(csvs)


if __name__ == "__main__":
    print("This is utils module")
