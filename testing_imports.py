# pylint: skip-file
# Poned aquí los imports de las funciones que hay que testear.
from modules.bmi import calculate_bmi
from modules.dictionaries import players_dict, clean_up_players_dict
from modules.evolution import top_average_column
from modules.statistics import find_max_col, find_rows_query
from modules.utils import read_add_year_gender, join_male_female, join_datasets_year
import pandas as pd
