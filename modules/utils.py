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
    data_frame = pd.read_csv(filepath)
    data_frame['gender'] = 'M' if gender == 'Male' else 'F'
    data_frame['year'] = year
    return data_frame


def join_male_female(path: str, year: int) -> pd.DataFrame:
    """
    - path: ruta a la carpeta que conté les dades
    - year: any del que es volen llegir les dades, format XXXX (per exemple, 2020)
    """
    os.chdir(path)
    extension = 'csv'
    year = get_small_year(year)
    all_filenames = [i for i in glob.glob(f'*{year}.{extension}')]
    csvs = []
    for i in all_filenames:
        temp = pd.read_csv(i)
        temp['gender'] = 'M' if 'female' not in i else 'F'
        temp['year'] = f'20{year}'
        csvs.append(temp)

    return pd.concat(csvs)


def join_datasets_year(path: str, years: list) -> pd.DataFrame:
    """
    - path: ruta a la carpeta que conté les dades
    - years: llista d’anys que es volen incloure en el dataframe, en format [XXXX,...]
    """
    os.chdir(path)
    extension = 'csv'
    all_filenames = []
    for year in years:
        year = get_small_year(year)
        all_filenames.append(list(glob.glob(f'*{year}.{extension}')))

    csvs = []
    for fi_name in all_filenames:
        for i in fi_name:
            temp = pd.read_csv(i)
            temp['gender'] = 'M' if 'female' not in i else 'F'
            year = ''.join(filter(str.isdigit, i))
            temp['year'] = int('20' + year)
            csvs.append(temp)

    return pd.concat(csvs)


if __name__ == "__main__":
    print("This is utils module")
    # join_male_female('data/', 2020)
    # join_datasets_year('data/', [2020, 2021])
