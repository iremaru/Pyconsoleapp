
# -----------------------
#       SCREEN FLOW - PUBLIC
# -----------------------

import main_menu_screen as main
import load_menu_screen as load

def set_first_screen(game_title :str):
    main.open(game_title)

def exit_app():
    """ TODO: Exit gameloop"""
    pass

def open_newgame_screen():
    """ TODO: open new game screen"""
    pass

def open_loadgame_screen():
    load.open()

def open_savegame_screen():
    """ TODO: open new game screen"""
    pass

def open_game_screen(is_new_game :bool):
    """ TODO: open game screen. Game screen must retrieves data from gamedata.py"""
    if is_new_game:
        __start_new_game()
    else:
        __load_game()
    


def returnto_game_screen():
    """ TODO: open new game screen"""
    pass

def returnto_mainmenu_screen():
    main.open()

# -----------------------
#       PRIVATE METHODS
# -----------------------

def __start_new_game():
    """ TODO: Move logic to gamedata.py"""
    pass

def __load_game():
    """ TODO: Move logic to gamedata.py"""
    pass
