import screenDecorator

answers = [
    'Sí',
    'Ciertamente',
    'Por supuesto que sí',
    'Sin la menor duda',
    'Puedes estar seguro/a',
    'Creo que sí',
    'Lo más seguro es que sí',
    'Todo apunta a que sí',
    'No estoy segura. Pregúntame más tarde',
    'Mejor no responder por ahora',
    'Ahora mismo es un poco dudoso',
    'Piensa en ello antes de preguntar de nuevo',
    'No',
    'Todo apunta a que no',
    'Tengo la impresión de que no',
    'Absolutamente, no',
    'Yo no contaría con ello',
    'Si quieres mi opinión, no',
    'Quizás',
    'Tú sabrás',
    'Piensa con el corazón, no con la cabeza',
    'Olvidate de eso',
]

def show():
    screenDecorator.show_line()
    screenDecorator.show_screen_title("Bienvenido a Bola Ocho")
    question = ask()
    answer(question)
    end()

def ask():
    screenDecorator.show_text("Haz una pregunta a la magnífica bola ocho.")
    screenDecorator.show_text("Pero si quires un consejo. Aprende a tomar tus propias decisiones.")
    return input("Pregunta: ")

def answer(question :str):
    import random
    question = question.lower().capitalize()
    screenDecorator.show_text(f'¿Así que quieres saber si \"{question}\"?')
    screenDecorator.show_text(f"Pues la bola ocho dice: {random.choice(answers)}")

def end():
    will_continued = input('¿Quieres hacer más preguntas? (S/N): ')
    will_continued.lower()
    if (will_continued == 'n') or (will_continued == 's'):
        if will_continued == 's':
            show()
    else:
        print("Eso no es una respuesta válida. Inténtalo de nuevo.")
        end()

    