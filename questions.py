import random

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

# Inicializamos el puntaje del usuario en 0
score = 0

# El usuario deberá contestar 3 preguntas
for _ in range(3):
    # Se selecciona una pregunta aleatoria
    question_index = random.randint(0, len(questions) - 1)

    # Se muestra la pregunta y las respuestas posibles
    print(questions[question_index])
    for i, answer in enumerate(answers[question_index]):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")

        # Se verifica que la respuesta sea válida
        if user_answer.isdigit() and 1<=int(user_answer)<=4:
            user_answer = int(user_answer) - 1
        else:
            # Si la respuesta es inválida se le informa al usuario y se
            # termina el programa con exit status igual a 1
            print("Respuesta no válida.")
            exit(1)

        # Se verifica si la respuesta es correcta, y si lo es,
        # se suma 1 punto al puntaje
        if user_answer == correct_answers_index[question_index]:
            score += 1
            print("¡Correcto!")
            break
        # Si la respuesta es incorrecta solo le restaremos 0.5 puntos si el
        # puntaje es mayor a 0 para evitar un puntaje negativo
        elif score!=0:
            score -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[question_index][correct_answers_index[question_index]])

    # Se imprime un blanco al final de la pregunta
    print()

# Se le muestra el puntaje final obtenido al usuario
print(f"Obtuviste un total de {score} puntos.")
