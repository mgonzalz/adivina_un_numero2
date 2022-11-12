def numeroaleatorio(minimo, maximo):
    import random
    numeroaleatorio = random.randint(minimo, maximo)
    return numeroaleatorio
def solicitar_numero_n1(minimo, maximo):
    minimo = 0
    maximo = 100
    while True:
        numero = solicitar_numero_n1("Introduzca un número entre", minimo,"y", maximo,": ")
        numero = input(numero)
        try:
            numero = int(numero)
        except:
            pass
        else:
            if minimo <= numero <= maximo:
                return nivel1
            else:
                print("El número debe estar entre", minimo, "y", maximo)
                return solicitar_numero_n1
def nivel1(minimo, numeroaleatorio, maximo):
    MINIMO = minimo
    MAXIMO = maximo
    intentos = int(0)
    while True:
        def adivinar_numero(numero, minimo, maximo):
            if numero < numeroaleatorio:
                print("Demasiado pequeño")
                intentos += 1
            elif numero > numeroaleatorio:
                print("Demasiado grande")
                intentos += 1
            else:
                print("Has acertado")
                return nivel1
            if intentos ==3:
                print(input("¿Necesitas alguna ayuda?"))
                if input == "si":
                    ayuda = "El número está entre {} y {}".format(minimo + 10, maximo -10)
                    print(ayuda)
                    return nivel2
                else:
                    return nivel1
def menu():
    print("1. Nivel 1")
    print("2. Nivel 2")
    print("3. Nivel 3")
    print("4. Nivel 4")
    print("5. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nivel1()
    elif opcion == "2":
        return nivel2
    elif opcion == "3":
        return nivel3
    elif opcion == "4":
        return nivel4
    elif opcion == "5":
        return salir
    else:
        print("Opción incorrecta")
        return menu
if __name__ == '__main__':
    print("El módulo se ejecuta")
    menu()
else:
    print("El módulo se ha importado")

#El primer cambio consiste en crear un menú que permita seleccionar un nivel de dificultad: nivel simple (entre 0 y 100), nivel intermedio (entre 0 y 1.000), nivel avanzado (entre 0 y 1.000.000) y nivel experto (entre 0 y 1.000.000.000.000). El jugador podrá escoger de manera sencilla su nivel, por ejemplo entre 1 y 4, y los valores mínimo y máximo se determinarán automáticamente. De manera opcional puede, sea cual sea el nivel, proponer al jugador una ayuda (mostrar el número mínimo y máximo deducidos de las anteriores entradas) o rechazarla. Puede crear una función para gestionar este menú, que incluirá en un nuevo módulo entrada.menu. También debe crear nuevas funciones en el módulo juego y revisar la función jugar. También es posible contar el número de intentos (y mostrarlo) y terminar la partida si se alcanza un valor máximo (que será libre de definir para cada nivel, aunque sea generoso). Al final de una partida ganada, puede también pedir al jugador su nombre y guardarlo en la tabla de mejores puntuaciones. En primer lugar, esta tabla se creará al inicio del programa y los datos se perderán una vez se cierre.
