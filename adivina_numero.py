def intro():
    print("ADIVINE EL NUMERO")
    print("1. Nivel Simple")
    print("2. Nivel Dificil")
    nivel = input("Introduzca el nivel de dificultad: ")
    if nivel == "1":
        print("Nivel Simple")
        print("El numero esta entre 0 y 100")
        juega(0, 100)
    else:
        print("Nivel Dificil")
        print("El numero esta entre 0 y 1000")
        juega(0, 1000)
def juega(minimo, maximo):
    import random
    numero = random.randint(minimo, maximo)
    print(numero)
    while True:
        print("Introduzca un numero entre", minimo, "y", maximo)
        intento = int(input())
        if intento == numero:
            print("Has acertado")
            break
        elif intento > numero:
            print("El numero es menor")
            maximo = intento - 1
        else:
            print("El numero es mayor")
            minimo = intento + 1
intro()
