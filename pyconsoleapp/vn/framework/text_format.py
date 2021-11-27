
# -----------------------
#       TEXT STYLE
# -----------------------
from termcolor import colored, cprint

def __blue_title(text :str):
    return colored(text, 'white', 'on_blue')

def __red_title(text :str):
    return colored(text, 'white', 'on_red')

def __green_title(text :str):
    return colored(text, 'white', 'on_green')


# -----------------------
#       CHARACTER MODEL
# -----------------------

class Character:
    def __init__(self, name :str, name_color, dialogue_color):
        self.name = name
        self.name_color = name_color
        self.dialogue_color = dialogue_color

# -----------------------
#       TEXT FORMAT
# -----------------------

__LINE_SCREEN_START =       '+----------+++--**--+++----------'
__LINE_SCREEN_END =         '+----------+----------+----------'
__LINE_DIALOGUE_START =     '+----------+/--*--*--\+----------'
__LINE_DIALOGUE_END =       '+----------+__________+----------'
__LINE_DIALOGUE_COLOR =     'green'
__LINE_SCREEN_COLOR =       'blue'

__NARRATION_DEFAULT_COLOR = 'white'
__DIALOGUE_DEFAULT_COLOR =  'white'
__TITLE_DEFAULT_COLOR =     'white'
__OPTION_DEFAULT_COLOR =    'green'

def new_screen_line():
    __show_line(__LINE_SCREEN_START, __LINE_SCREEN_COLOR)
    __show_line(__LINE_SCREEN_START, __LINE_SCREEN_COLOR)

def end_screen_line():
    __show_line(__LINE_SCREEN_END, __LINE_SCREEN_COLOR)
    __show_line(__LINE_SCREEN_END, __LINE_SCREEN_COLOR)

def title(text :str):
    """Show title in the screen"""
    text = text.upper()
    __show_text(text, __TITLE_DEFAULT_COLOR)

def narration(text :str, pov :Character):
    __show_text(pov.name, pov.name_color)
    __show_text(text)

def dialogue(text :str, character_name = 'Unknown'):
    __show_line(__LINE_DIALOGUE_START, __LINE_DIALOGUE_COLOR)
    __show_text(character_name, __DIALOGUE_DEFAULT_COLOR)
    __show_text(text, __DIALOGUE_DEFAULT_COLOR)
    __show_line(__LINE_DIALOGUE_END, __LINE_DIALOGUE_COLOR)

def dialogue(text :str, character :Character):
    __show_line(__LINE_DIALOGUE_START, __LINE_DIALOGUE_COLOR)
    __show_text(character.name, character.name_color)
    __show_text(text, character.dialogue_color)
    __show_line(__LINE_DIALOGUE_END, __LINE_DIALOGUE_COLOR)

def monologue(texts :list, character :Character):
    __show_line(__LINE_DIALOGUE_START, __LINE_DIALOGUE_COLOR)
    __show_text(character.name, character.name_color)
    for dialogue in texts:
        __show_text(dialogue, character.dialogue_color)
    __show_line(__LINE_DIALOGUE_END, __LINE_DIALOGUE_COLOR)

def option(text):
    cprint(text, __OPTION_DEFAULT_COLOR)

def __show_text(text :str, color = __NARRATION_DEFAULT_COLOR):
    cprint(text, color)

def __show_line(line_type :str, on_color :str):
    cprint(line_type, 'white', on_color)
