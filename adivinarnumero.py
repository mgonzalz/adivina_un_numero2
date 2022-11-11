def nivel1(simple):
    minimo = 0
    maximo = 100
    import random
    numeroaleatorio = random.randint(minimo, maximo)
    intentos = 0
    pistas = 0
    while True:
        numero = input("Adivina el número: ")
        try:
            numero = int(numero)
        except:
            pass
        else:
            if minimo <= numero <= maximo:
                break
    while True:
        if numero < numeroaleatorio:
            print("Demasiado pequeño")
            intentos += 1
            pistas += 1
        elif numero > numeroaleatorio:
            print("Demasiado grande")
            intentos += 1
            pistas += 1
        else: # numero == numeroaleatorio
            print("¡Has acertado!")
            break
    while True:
        if pistas == 3:
            print(input("¿Quieres alguna pista?: "))





#El primer cambio consiste en crear un menú que permita seleccionar un nivel de dificultad: nivel simple (entre 0 y 100), nivel intermedio (entre 0 y 1.000), nivel avanzado (entre 0 y 1.000.000) y nivel experto (entre 0 y 1.000.000.000.000). El jugador podrá escoger de manera sencilla su nivel, por ejemplo entre 1 y 4, y los valores mínimo y máximo se determinarán automáticamente. De manera opcional puede, sea cual sea el nivel, proponer al jugador una ayuda (mostrar el número mínimo y máximo deducidos de las anteriores entradas) o rechazarla. Puede crear una función para gestionar este menú, que incluirá en un nuevo módulo entrada.menu. También debe crear nuevas funciones en el módulo juego y revisar la función jugar. También es posible contar el número de intentos (y mostrarlo) y terminar la partida si se alcanza un valor máximo (que será libre de definir para cada nivel, aunque sea generoso). Al final de una partida ganada, puede también pedir al jugador su nombre y guardarlo en la tabla de mejores puntuaciones. En primer lugar, esta tabla se creará al inicio del programa y los datos se perderán una vez se cierre.
