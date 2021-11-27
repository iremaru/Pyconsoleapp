from Gameapp.gameapp.vn.framework.text_format import title
import text_format

# -----------------------
#       MAIN MENU SCREEN MODEL
# -----------------------

__main_menu_options = [
    {
        'code': 'new_game',
        'text': 'New game'
    },
    {
        'code': 'load_game',
        'text': 'Load game'
    },
    {
        'code': 'exit',
        'text': 'Exit'
    },
    
]

def __add_menu_options(options :list):
    for option in options:
        __main_menu_options.append(option)

def __get_menu_options():
    return __main_menu_options

def __get_menu_option(option_index :int):
    return __main_menu_options[option_index]

def __get_menu_option(option_name :str):
    return __get_menu_option( __main_menu_options.index(option_name) )


# -----------------------
#       MAIN MENU SCREEN VIEWS
# -----------------------

def open_main_menu(game_name = 'Novela Visual'):
    
    title(game_name)
    for option in __main_menu_options:
        name = option['text'].lower()
        option(f'Press [] to { name }')


# -----------------------
#       MAIN MENU SCREEN ACTIONS
# -----------------------

def select_menu_option(option :int):
    option = __main_menu_options[option]
    if option == 0 :
        start_new_game()
    if option == 1 :
        open_load_menu()
    if option == 2 :
        exit_game()