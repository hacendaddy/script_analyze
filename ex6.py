"""This module executes exercice 6 (Not finished)"""

import random
from modules import utils, dictionaries

"""
Input - 2022 Males and females
Output
    Male:
        - 4 players "player_positions": (2 central "CB", 1 right "RB", 1 left "LB")
    Female:
        - 4 players "player_positions": (2 central "CB", 1 right "RB", 1 left "LB")
    Mixt:
        - 4 players "player_positions": (2 central "CB", 1 right "RB", 1 left "LB")

No repetitions
Que aporta cada posicio (defending, skill_ball_control, physic)
"""

if __name__ == "__main__":
    DATA_FRAME = utils.join_male_female("data/", 2022)
    DATA_FRAME = DATA_FRAME.loc[(DATA_FRAME["player_positions"] == "CB") | (DATA_FRAME["player_positions"] == "LB")
                                | (DATA_FRAME["player_positions"] == "RB")]
    DF_DICT = dictionaries.players_dict(DATA_FRAME, DATA_FRAME["sofifa_id"].unique(),
                                        ["short_name", "player_positions", "defending",
                                         "skill_ball_control", "physic"])
    COL_QUERY = [("short_name", "del_rep")]
    DF_DICT = dictionaries.clean_up_players_dict(DF_DICT, COL_QUERY)
    # pprint(df_dic)

    # Positions
    RB_PLAYERS = []
    LB_PLAYERS = []
    CB_PLAYERS = []

    # Seen
    PLAYERS = []

    while len(PLAYERS) != 16:
        TEMP_CHOSEN = random.choice(list(DF_DICT.values()))
        if 'RB' in TEMP_CHOSEN.get('player_positions'):
            RB_PLAYERS.append(TEMP_CHOSEN)
        elif 'LB' in TEMP_CHOSEN.get('player_positions'):
            LB_PLAYERS.append(TEMP_CHOSEN)
        else:
            CB_PLAYERS.append(TEMP_CHOSEN)
        PLAYERS.append(TEMP_CHOSEN)

    RB_CHOICE = random.choice(RB_PLAYERS)
    LB_CHOICE = random.choice(LB_PLAYERS)
    CB1_CHOICE = random.choice(CB_PLAYERS)
    CB2_CHOICE = random.choice(CB_PLAYERS)

    print("Dreta", RB_CHOICE)
    print("Esquerra", LB_CHOICE)
    print("Central 1", CB1_CHOICE)
    print("Central 2", CB2_CHOICE)
