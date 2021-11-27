import screenDecorator
import screenManager
import score

__isRunning__ = True

def init_app():
    score.load_score()
    __start_app__()

def __start_app__():
    global __isRunning__
    __isRunning__ = True
    while(__isRunning__):
        screenManager.load_screen('m')

def stop_app():
    global __isRunning__
    screenDecorator.show_line()
    screenDecorator.show_text('Adios. Fue un placer tenerte por aqui.')
    __isRunning__ = False
