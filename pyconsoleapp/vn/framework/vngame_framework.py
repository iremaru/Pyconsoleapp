import json

__SCENES__ = []
__STATS__ = {
    'gameText': {},
    'historyAtStart': {
        'conditions': {
            'toStartScene' : {},
            'others' : {}},
        'characters' : {
            'mainCharacter': {
                'name': 'Prota',
                'health': 100 
            },
            'characterA' : {
                'name': '',
                'health': 100,
                'friendPoints': 0,
            },
            'characterB' : {
                'name': '',
                'health': 100,
                'friendPoints': 0,
            }
        },
    },
    'historyCurrently': [
        {
            'name': '',
            'data': {}
        }
    ]
}
__SAVE_FILE_PATH__ = ''
__SAVE_FILE_NAME__ = ''
__SAVE_FILE_DATA__ = []
__DEFAULT_NEW_GAME_NAME__ = 'New Game'

def init_game(scenes :list):
    global __SCENES__   
    __SCENES__ = scenes
    __fill_save_file_data()

def exit_game():
    """ TODO: """
    pass

# -----------------------
#       GAME FLOW
# -----------------------

def __start_game(is_new_game :bool, game_name :str):
    if is_new_game:
        __start_new_game(__DEFAULT_NEW_GAME_NAME__)
    else:
        __load_game(game_name)

def __start_new_game(game_name :str):
    __generate_save_file()

def __load_game(game_name :str):
    if len(__SAVE_FILE_DATA__) == 0 :
        __err_empty_save_data()
    if len(__SAVE_FILE_DATA__) == 1 :
        __SAVE_FILE_DATA__[0]
    else:
        for save in __SAVE_FILE_DATA__:
            if save['name'] == game_name:
                save['data']

def __end_game():
    """ TODO: """
    pass

# -----------------------
#       DATA PERSISTENCE
# -----------------------
def __generate_save_file():
    with open(__SAVE_FILE_PATH__ + __SAVE_FILE_NAME__, 'w') as save_file:
        save_file.write( json.dumps(__STATS__['historyAtStart']) )

def __fill_save_file_data():
    with open(__SAVE_FILE_PATH__ + __SAVE_FILE_NAME__, 'w') as save_file:
        global __SAVE_FILE_DATA__
        __SAVE_FILE_DATA__ = json.loads( save_file.read() )
    

def save_game():
    with open(__SAVE_FILE_PATH__ + __SAVE_FILE_NAME__, 'w') as save_file:
        save_file.write( json.dumps(__STATS__['historyCurrently']) )


# -----------------------
#       STORY FORMAT
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