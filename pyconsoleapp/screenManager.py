import menu, app, screenDecorator, score, eightball, os

SCREEN_DIRECTORY = { 
    'menu':     'M',
    'bola':     'B',
    'novela':   'N',
    'rol':      'R',
    'puntaje':  'P',
    'salir':    'X'
    }
def change_screen():
    user_option = input('Escribe el código de la opción: ')
    load_screen(user_option)

def load_screen(screen_code :str):
    os.system('cls')
    global SCREEN_DIRECTORY
    screen_code = screen_code.upper()
    if(screen_code == SCREEN_DIRECTORY['menu']):
        return menu.show()
    if(screen_code == SCREEN_DIRECTORY['bola']):
        return eightball.show()
    if(screen_code == SCREEN_DIRECTORY['novela']):
        return menu.show()
    if(screen_code == SCREEN_DIRECTORY['rol']):
        return menu.show()
    if(screen_code == SCREEN_DIRECTORY['puntaje']):
        return score.show()
    if(screen_code == SCREEN_DIRECTORY['salir']):
        return app.stop_app()
    
    screenDecorator.show_text('Esa opción no es válida. Elige otra')
    return change_screen()