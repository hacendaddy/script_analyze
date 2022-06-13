from testing_imports import *


def fill_empty_slots(data: list, leng: int) -> list:
    """Fills with 0s the no data for the other years

    Args:
        data (list): values with missing data
        leng (int): lenght to be

    Returns:
        list: filled data
    """
    while len(data) != leng:
        data.append(0)
    return data


def autolabel(rects: matplotlib.container.BarContainer) -> None:
    """Attach a text label above each bar in *rects*, displaying its height.

    Args:
        rects (matplotlib.container.BarContainer): Container for the artists of bar plots
    """
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


if __name__ == "__main__":
    print("Exercici 2c")

    DATA_FRAME = join_datasets_year("data", list(range(2016, 2023)))
    COLS_TO_RETURN = ["short_name", "year", "age", "overall", "potential"]

    print('Jugador Belga < de 25 amb màxim potential:')
    QUERY = (['nationality_name', 'age'], ['Belgium', (0, 24)])
    print(find_max_col(find_rows_query(DATA_FRAME, QUERY, COLS_TO_RETURN),
                       "potential", COLS_TO_RETURN), "\n")

    print('Porteres >= de 28 anys amb overall >= a 85:')
    QUERY = (["player_positions", "age", "overall", "gender"],
             ["GK", (28, 100), (85, 100), "F"])
    print(find_rows_query(DATA_FRAME, QUERY, COLS_TO_RETURN))

    print("-" * 50)
    print("Exercici 3a i 3b")

    DATA_FRAME = join_datasets_year('data', [2022])
    INE = pd.read_csv(os.path.join("data", "INE.csv"), sep=";", thousands=",")

    DATA = calculate_bmi(DATA_FRAME, 'M', 2022, ["sofifa_id", "club_flag_url"])
    PREP_DATA = DATA.groupby(DATA['club_flag_url'].str.slice(
        29, -4))['BMI'].max().reset_index()
    c = ['red', 'yellow', 'black', 'blue', 'orange']

    # Plot FIFA per país
    plt.subplot(1, 2, 1)  # row 1, col 2 index 1
    plt.bar(PREP_DATA["club_flag_url"],
            PREP_DATA["BMI"], color="pink", alpha=0.25)
    plt.axhline(y=18.5, color=c[0], linestyle='-')
    plt.axhline(y=24, color=c[1], linestyle='-')
    plt.axhline(y=25, color=c[2], linestyle='-')
    plt.axhline(y=30, color=c[3], linestyle='-')
    plt.title("Dades FIFA BMI")
    plt.xticks(rotation=90)

    # Plot BMI explicatiu població española
    plt.subplot(1, 2, 2)  # index 2
    INE = INE.loc[INE["Adult body mass index"] != "TOTAL"]
    INE["mass_group"] = INE['Adult body mass index'].str.replace(
        r"\([^()]*\)", '', regex=True).str.strip()
    plt.bar(INE["mass_group"], INE["Total"], color=c)

    colors = {
        'Underweight < 18.5': 'red',
        'Normal weight [18.5, 25)': 'yellow',
        'Overweight [25, 30)': 'black',
        'Obese ≥ 30': 'blue'
    }
    labels = list(colors.keys())
    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[label])
               for label in labels]
    plt.legend(handles, labels)

    plt.title("Dades població (H/D) BMI 2020 Espanya per categories")
    plt.xticks(rotation=45)

    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)

    plt.show()

    print("""
    Podem veure com l'únic país que no arriba a overweight es chipre a les dades del FIFA, els altres si fèssim cas purament
          a les dades, pensariem que els futbolistes estan en molt mala forma, però els esportistes d'èlit tenen massa muscular
          i el BMI no ho té en compte.
    """)

    print("-" * 50)
    print("Exercici 4c")

    DATA_FRAME = join_datasets_year("data", [2016, 2017, 2018])
    COLS = ['short_name', 'overall', 'potential', 'player_positions', 'year']
    IDS = [226328, 192476, 230566]

    PLAYER_DICT = players_dict(DATA_FRAME, IDS, COLS)

    print("Diccionari:")
    pprint(PLAYER_DICT)

    print("\nQuery:")
    COL_QUERY = [("player_positions", "del_rep"), ("short_name", "one")]
    print(COL_QUERY)

    print("\nDiccionari net:")
    CLEAN_DICT = clean_up_players_dict(PLAYER_DICT, COL_QUERY)
    pprint(CLEAN_DICT)

    print("-" * 50)
    print("Exercici 5b")

    DATA_FRAME = join_datasets_year(
        "data", [2016, 2017, 2018, 2019, 2020, 2021, 2022])
    COLS = ['short_name', 'year', 'movement_sprint_speed']
    PLAYER_DICT = players_dict(
        DATA_FRAME, DATA_FRAME['sofifa_id'].unique(), COLS)

    COL_QUERY = [("short_name", "one")]
    CLEAN_DICT = clean_up_players_dict(PLAYER_DICT, COL_QUERY)

    AVERAGE_RESULT = top_average_column(
        CLEAN_DICT, 'short_name', 'movement_sprint_speed', len(range(2016, 2023)))
    pprint(AVERAGE_RESULT[:4])

    ################
    labels = ["2016", "2017", "2018", "2019", "2020", "2021", "2022"]

    barWidth = 0.25
    N = 4

    player_names = []
    for v in AVERAGE_RESULT[:N]:
        player_names.append(v[0])

    player1 = (fill_empty_slots(
        AVERAGE_RESULT[:N][0][2]['value'], len(labels)))
    player2 = (fill_empty_slots(
        AVERAGE_RESULT[:N][1][2]['value'], len(labels)))
    player3 = (fill_empty_slots(
        AVERAGE_RESULT[:N][2][2]['value'], len(labels)))
    player4 = (fill_empty_slots(
        AVERAGE_RESULT[:N][3][2]['value'], len(labels)))

    r1 = np.arange(len(player1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]

    fig, ax = plt.subplots(1, 1, figsize=(15, 7))

    p1 = ax.bar(r1, player1, color='red', align='center',
                width=barWidth, edgecolor='white', label=player_names[0])
    p2 = ax.bar(r2, player2, color='green', align='center',
                width=barWidth, edgecolor='white', label=player_names[1])
    p3 = ax.bar(r3, player3, color='blue', align='center',
                width=barWidth, edgecolor='white', label=player_names[2])
    p4 = ax.bar(r4, player4, color='purple', align='center',
                width=barWidth, edgecolor='white', label=player_names[3])

    autolabel(p1)
    autolabel(p2)
    autolabel(p3)
    autolabel(p4)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_title('Distribució anual de movement sprint speed')
    plt.xlabel('Anys', fontweight='bold')
    ax.set_ylabel('Movement sprint speed')
    plt.xticks([r + barWidth for r in range(len(player1))], labels)

    # Create legend & Show graphic
    ax.legend(loc=(1.04, 0))
    plt.subplots_adjust(right=0.8)
    plt.show()
