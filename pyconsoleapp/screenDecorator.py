from termcolor import colored, cprint

SCREEN_WIDTH = '80'
ALIGN_CENTER = '{:^' + SCREEN_WIDTH + '}'
ALIGN_LEFT = '{:<' + SCREEN_WIDTH + '}'


def show_line(steps=4):
    PATTERN_A_SIDE =    "*__*--*__*"
    PATTERN_A_MIDDLE =  "*--*__*--*"

    line = PATTERN_A_SIDE

    if(steps > 0):
        for i in range(1, steps):
            if (i % 2 == 0):
                line += PATTERN_A_SIDE
            else:
                line += PATTERN_A_MIDDLE

    line += PATTERN_A_SIDE

    line = colored(line, 'yellow')
    print(ALIGN_CENTER.format(line))

def show_screen_title(text: str):
    text = text.upper()
    print(ALIGN_CENTER.format(text))

def show_text(text: str):
    TEXT_F = ' '*4
    text = TEXT_F + ALIGN_LEFT.format(text)
    print(text)

def show_option(option_sign: str, option_text: str, color = 'blue'):
    OPTION_MARGIN = ' '*8
    OPTION_SIGN = colored('[' + option_sign + ']', color)
    OPTION_TEXT = colored(option_text, 'cyan')
    OPTION = OPTION_MARGIN + OPTION_SIGN + ' - ' + OPTION_TEXT
    TEXT_FORMATTED = ALIGN_LEFT.format(OPTION)
    cprint(TEXT_FORMATTED)

