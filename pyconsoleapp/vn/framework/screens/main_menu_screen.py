from screen_flow import exit_app as exit
from screen_flow import open_newgame_screen as new_game
from screen_flow import open_loadgame_screen as load_game

from pyconsoleapp.vn.framework.text_format import title

# -----------------------
#       MAIN MENU SCREEN MODEL
# -----------------------

__main_menu_options__ = [
    {
        'code': new_game,
        'text': 'New game',
        'key':  'N'
    },
    {
        'code': load_game,
        'text': 'Load game',
        'key':  'L'
    },
    {
        'code': exit,
        'text': 'Exit',
        'key': 'X'
    },
    
]

def __add_menu_options(options :list):
    for option in options:
        __main_menu_options__.append(option)

def __get_menu_options():
    return __main_menu_options__

def __get_menu_option(option_index :int):
    return __main_menu_options__[option_index]

def __get_menu_option(option_name :str):
    return __get_menu_option( __main_menu_options__.index(option_name) )


# -----------------------
#       MAIN MENU SCREEN - PUBLIC INTERNAL
# -----------------------

def open(game_title :str):
    title(game_title)
    for option in __main_menu_options__:
        name = option['text'].lower()
        key = option['key']
        option(f'Press { key } to { name }')
    user_option = input("Select an optión")
    select_menu_option(user_option)


# -----------------------
#       MAIN MENU SCREEN - PUBLIC BUILD CUSTUMIZATION
# -----------------------


def add_option(code :function, text :str, key :str):
    """Add options to the main menu in build or at runtime.
    Return True if it is done; Return false if it can't be done."""
    global __main_menu_option
    # TODO: Test if "warnings" module works in this way
    for option in __main_menu_options__:
        if ( option['text'] == text ):
            import warnings
            warnings.warn('You are trying to use \"{text}\" in an option at Main Menu, but this name is in use')
            return False

        if ( option['key'] == key ):
            import warnings
            warnings.warn(f"{option['text']} is using \"{key}\" as key, too.")
            return False
    __main_menu_options__.append(
        {
            'code': code,
            'text': text,
            'key': key.upper()
        }
    )
    return True
    

# -----------------------
#       MAIN MENU SCREEN ACTIONS
# -----------------------

def select_menu_option(choosen_option :str):
    answer = choosen_option.lower()
    for option in __main_menu_options__:
        if option['key'] == answer:
            option['code']()
