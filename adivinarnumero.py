
def nivel(maximo, minimo):
    while True:
        print("1. Nivel Simple (entre 0 y 100)")
        print("2. Nivel Intermedio (entre 0 y 1.000)")
        print("3. Nivel Avanzado (entre 0 y 1.000.000)")
        print("4. Nivel Experto (entre 0 y 1.000.000.000.000)")
        print("5. Salir")
        nivel = input("¿Qué nivel desea jugar?")
        print(nivel)
        if nivel == "1" "Nivel Simple":
            maximo = 100
            minimo = 0
            return maximo, minimo
        elif nivel == "2" "Nivel Intermedio":
            maximo = 1000
            minimo = 0
            return maximo, minimo
        elif nivel == "3" "Nivel Avanzado":
            maximo = 1000000
            minimo = 0
            return maximo, minimo
        elif nivel == "4" "Nivel Experto":
            maximo = 1000000000000
            minimo = 0
            return maximo, minimo
        elif nivel == "5" "Salir":
            print("¡Hasta pronto!")
            return


def jugar():
    minimo, maximo = nivel()
#El primer cambio consiste en crear un menú que permita seleccionar un nivel de dificultad: nivel simple (entre 0 y 100), nivel intermedio (entre 0 y 1.000), nivel avanzado (entre 0 y 1.000.000) y nivel experto (entre 0 y 1.000.000.000.000). El jugador podrá escoger de manera sencilla su nivel, por ejemplo entre 1 y 4, y los valores mínimo y máximo se determinarán automáticamente. De manera opcional puede, sea cual sea el nivel, proponer al jugador una ayuda (mostrar el número mínimo y máximo deducidos de las anteriores entradas) o rechazarla. Puede crear una función para gestionar este menú, que incluirá en un nuevo módulo entrada.menu. También debe crear nuevas funciones en el módulo juego y revisar la función jugar. También es posible contar el número de intentos (y mostrarlo) y terminar la partida si se alcanza un valor máximo (que será libre de definir para cada nivel, aunque sea generoso). Al final de una partida ganada, puede también pedir al jugador su nombre y guardarlo en la tabla de mejores puntuaciones. En primer lugar, esta tabla se creará al inicio del programa y los datos se perderán una vez se cierre.
