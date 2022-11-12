def numeroaleatorio(minimo, maximo):
    import random
    numeroaleatorio = random.randint(minimo, maximo)
    return numeroaleatorio
def solicitar_numero(minimo, maximo):
    minimo = 0
    maximo = 100
    while True:
        numero = solicitar_numero("Introduzca un número entre", minimo,"y", maximo,": ")
        numero = input(numero)
        try:
            numero = int(numero)
        except:
            pass
        else:
            if minimo <= numero <= maximo:
                return numero
            else:
                print("El número debe estar entre", minimo, "y", maximo)
def nivel1(minimo, maximo):
    intentos = int(0)
    while True:
        def adivinar_numero(numero, minimo, maximo):
            if numero < numeroaleatorio:
                print("Demasiado pequeño")
            elif numero > numeroaleatorio:
                print("Demasiado grande")
            else:
                print("Has acertado")
def menu():
    print("1. Nivel Simple")
    print("2. Nivel Intermedio")
    print("3. Nivel Avanzado")
    print("4. Nivel Experto")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nivel1(0, 100)
        numeroaleatorio(0, 100)
    elif opcion == "2":
        nivel1(0, 1000)
    elif opcion == "3":
        nivel1(0, 1000000)
    elif opcion == "4":
        nivel1(0, 1000000000000)
    else:
        print("Opción incorrecta")
        return menu
if __name__ == '__main__':
    print("El módulo se ejecuta")
    menu()
else:
    print("El módulo se ha importado")

#El primer cambio consiste en crear un menú que permita seleccionar un nivel de dificultad: nivel simple (entre 0 y 100), nivel intermedio (entre 0 y 1.000), nivel avanzado (entre 0 y 1.000.000) y nivel experto (entre 0 y 1.000.000.000.000). El jugador podrá escoger de manera sencilla su nivel, por ejemplo entre 1 y 4, y los valores mínimo y máximo se determinarán automáticamente. De manera opcional puede, sea cual sea el nivel, proponer al jugador una ayuda (mostrar el número mínimo y máximo deducidos de las anteriores entradas) o rechazarla. Puede crear una función para gestionar este menú, que incluirá en un nuevo módulo entrada.menu. También debe crear nuevas funciones en el módulo juego y revisar la función jugar. También es posible contar el número de intentos (y mostrarlo) y terminar la partida si se alcanza un valor máximo (que será libre de definir para cada nivel, aunque sea generoso). Al final de una partida ganada, puede también pedir al jugador su nombre y guardarlo en la tabla de mejores puntuaciones. En primer lugar, esta tabla se creará al inicio del programa y los datos se perderán una vez se cierre.
