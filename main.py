from testing_imports import *

if __name__ == "__main__":
    print("Exercici 2c")

    DATA_FRAME = join_datasets_year("data", list(range(2016, 2023)))
    COLS_TO_RETURN = ["short_name", "year", "age", "overall", "potential"]

    print('Jugador Belga < de 25 amb màxim potential:')
    QUERY = (['nationality_name', 'age'], ['Belgium', (0, 24)])
    print(find_max_col(find_rows_query(DATA_FRAME, QUERY, COLS_TO_RETURN),
                       "potential", COLS_TO_RETURN), "\n")

    print('Porteres >= de 28 anys amb overall >= a 85:')
    QUERY = (["player_positions", "age", "overall", "gender"], ["GK", (28, 100), (85, 100), "F"])
    print(find_rows_query(DATA_FRAME, QUERY, COLS_TO_RETURN))

    print("-" * 50)
    print("Exercici 3a")

    DATA_FRAME = join_datasets_year('data', [2022])
    DATA = calculate_bmi(DATA_FRAME, 'M', 2022, ["sofifa_id", "club_flag_url"])

    PREP_DATA = DATA.groupby(DATA['club_flag_url'].str.slice(
        29, -4))['BMI'].max().reset_index()
    plt.bar(PREP_DATA["club_flag_url"], PREP_DATA["BMI"])
    plt.xticks(rotation=90)
    plt.show()

    print("-" * 50)
    print("Exercici 3b")
    INE = pd.read_csv(os.path.join("data", "INE.csv"), sep=";", thousands=",")
    print(INE.head())
    # TODO:: Finalitzar

    print("-" * 50)
    print("Exercici 4c")
    DATA_FRAME = join_datasets_year("data", [2016, 2017, 2018])
    COLS = ['short_name', 'overall', 'potential', 'player_positions', 'year']
    IDS = [226328, 192476, 230566]

    PLAYER_DICT = players_dict(DATA_FRAME, IDS, COLS)

    print("Diccionari:")
    pprint(PLAYER_DICT)

    print("Query:")
    COL_QUERY = [("player_positions", "del_rep"), ("short_name", "one")]
    print(COL_QUERY)

    print("Diccionari net:")
    CLEAN_DICT = clean_up_players_dict(PLAYER_DICT, COL_QUERY)
    pprint(CLEAN_DICT)

    print("-" * 50)
    print("Exercici 5b")

    # TODO:: Improve
    # Obtenim totes les dades necessàries fins ara
    DATA_FRAME = join_datasets_year("data", [2016, 2017, 2018, 2019, 2020, 2021, 2022])
    COLS = ['short_name', 'year', 'movement_sprint_speed']
    PLAYER_DICT = players_dict(DATA_FRAME, DATA_FRAME['sofifa_id'].unique(), COLS)

    COL_QUERY = [("short_name", "one")]
    CLEAN_DICT = clean_up_players_dict(PLAYER_DICT, COL_QUERY)

    # function
    RESULT = top_average_column(CLEAN_DICT, 'short_name', 'movement_sprint_speed', 7)
    pprint(RESULT[:4])

    plt.rcParams["figure.figsize"] = (15, 10)
    line_style = ["-", "--", "-.", ":", "^"]
    for i, top_value in enumerate(RESULT[:4]):
        plt.plot(
            RESULT[:4][i][2]['year'],
            RESULT[:4][i][2]['value'],
            label=RESULT[:4][i][0],
            linestyle=line_style[i]
        )
    plt.ylabel("Movement Sprint Speed")
    plt.xlabel("Any")
    plt.legend()
    plt.show()
