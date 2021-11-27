from screens.screen_flow import set_first_screen
from data_persistence import fill_save_file_data


__is_running = True

def init_game(scenes :list):
    global __SCENES__   
    __SCENES__ = scenes
    fill_save_file_data()
    __start_game_loop()

def exit_game():
    global __is_running
    __is_running = False

def __start_game_loop():
    while(__is_running):
        """ TODO: GAME LOGIC"""
        set_first_screen()

# -----------------------
#       STORY RUNNER
# -----------------------

def show_scenary():
    """ TODO: """
    pass

def tell_scene(scene_position :int):
    """ TODO: """
    pass

# -----------------------
#       ERROR CATCHS
# -----------------------

def __err_empty_save_data():
    """ TODO: """
    pass 

def __err_save_game_not_found():
    """ TODO: """
    pass