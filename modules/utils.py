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
        temp = pd.read_csv(i, low_memory=False)
        temp['gender'] = 'M' if 'female' not in i else 'F'
        temp['year'] = int(f'20{year}')
        csvs.append(temp)

    return pd.concat(csvs)


def join_datasets_year(path: str, years: list) -> pd.DataFrame:
    """
    - path: ruta a la carpeta que conté les dades
    - years: llista d’anys que es volen incloure en el dataframe, en format [XXXX,...]
    """
    all_filenames = []
    for year in years:
        year = get_small_year(year)
        new_path = os.path.join(f"{path}", f'*{year}.csv')
        all_filenames.append(list(glob.glob(new_path)))

    csvs = []
    for fi_name in all_filenames:
        for i in fi_name:
            temp = pd.read_csv(i, low_memory=False)
            temp['gender'] = 'M' if 'female' not in i else 'F'
            year = ''.join(filter(str.isdigit, i))
            temp['year'] = int(f'20{year}')
            csvs.append(temp)

    return pd.concat(csvs)


if __name__ == "__main__":
    print("This is utils module")
    # print(join_male_female('data', 2020).shape)
    # join_datasets_year('data/', [2020, 2021])
