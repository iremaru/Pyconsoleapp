from pyconsoleapp.vn.framework.text_format import end_screen_line, narration, new_screen_line, option, title
from data_persistence import get_save_game_list as game_list
from screen_flow import returnto_mainmenu_screen, open_game_screen

# -----------------------
#       LOAD MENU SCREEN
# -----------------------

__save_games__ = []

def open():
    new_screen_line()
    title("Load Game")
    __show_save_games()
    option('Press "R" to return to main menu.')
    end_screen_line()
    __ask_to_player_for_choose()

def __show_save_games():
    global __save_games__
    __save_games__ = game_list()
    if len(__save_games__) < 1:
        narration("There are not save games. Sorry.")
    else:
        for i in range(1, len(__save_games__)):
            option(f'Press [{i}] to open \"{ __save_games__[i]["name"] }\"')

def __ask_to_player_for_choose():
    user_answer = input("¿What do you choose?: ")
    __catch_user_answer(user_answer)

def __catch_user_answer(user_answer :str):
    user_answer = user_answer.upper()
    if user_answer == "X":
        returnto_mainmenu_screen()
    if user_answer.isdigit():
        open_game_screen(False)
    if not user_answer.isdigit():
        narration("You should use the number asigned to the game.")
        __ask_to_player_for_choose()