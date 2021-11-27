import screenDecorator, screenManager

def show():
    screenDecorator.show_line()
    screenDecorator.show_screen_title('Menú')
    screenDecorator.show_text("Elige lo que quieres hacer:")
    screenDecorator.show_option('S', 'Sumar números')
    screenDecorator.show_option('C', 'Ver un chiste')
    screenDecorator.show_option('B', 'Bola Ocho')
    screenDecorator.show_option('P', 'Ver la puntuación')
    screenDecorator.show_option('X', 'Salir', 'red')
    screenManager.change_screen()
