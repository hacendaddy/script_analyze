from modules import utils, dictionaries, evolution
from pprint import pprint
import random

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
    df = utils.join_male_female("data/", 2022)
    df = df.loc[(df["player_positions"] == "CB") | (df["player_positions"] == "LB") | (df["player_positions"] == "RB")]
    df_dic = dictionaries.players_dict(df, df["sofifa_id"].unique(),
                                       ["short_name", "player_positions", "defending", "skill_ball_control", "physic"])
    col_query = [("short_name", "del_rep")]
    df_dic = dictionaries.clean_up_players_dict(df_dic, col_query)
    # pprint(df_dic)

    # Positions
    rb_players = []
    lb_players = []
    cb_players = []

    # Seen
    players = []

    while len(players) != 16:
        temp_chosen = random.choice(list(df_dic.values()))
        if 'RB' in temp_chosen.get('player_positions'):
            rb_players.append(temp_chosen)
        elif 'LB' in temp_chosen.get('player_positions'):
            lb_players.append(temp_chosen)
        else:
            cb_players.append(temp_chosen)
        players.append(temp_chosen)

    rb = random.choice(rb_players)
    lb = random.choice(lb_players)
    cb1 = random.choice(cb_players)
    cb2 = random.choice(cb_players)
