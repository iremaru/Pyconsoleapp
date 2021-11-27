import screenDecorator

current_score = 0
SAVE_PATH = "score.txt"

def load_score():
    global current_score
    with open(SAVE_PATH) as saveFile:
        current_score = int(saveFile.read())

def update_score(added_score : int):
    global current_score
    current_score += added_score

def show():
    screenDecorator.show_line()
    screenDecorator.show_text(f"Tu puntuación actual es {current_score}")
    screenDecorator.show_line()

def save():
    with open(SAVE_PATH, 'w') as saveFile:
        screenDecorator.show_text("Puntuación guardada")
        global current_score
        saveFile.write( str(current_score) )

