def intro():
    print ("ADIVINE EL NUMERO")
    print ("***" * 10)
    print ("1. Nivel Simple (0-100)")
    print ("2. Nivel Intermedio (0-1000)")
    print ("3. Nivel Avanzado (0-1.000.000)")
    print ("4. Nivel Experto (0 y 1.000.000.000.000)")
    print ("5. Salir")
    nivel = input("Introduzca el nivel de dificultad: ")
    if nivel == "1":
        juega(0, 100)
    elif nivel == "2":
        juega(0, 1000)
    elif nivel == "3":
        juega(0, 1000000)
    elif nivel == "4":
        juega(0, 1000000000000)
    elif nivel == "5":
        print("Gracias por jugar")
        exit()
    else:
        intro()
def juega(minimo, maximo):
    import random
    numero = random.randint(minimo, maximo)
    print(numero)
    ayuda = 0
    while True:
        print("Introduzca un numero entre", minimo, "y", maximo)
        intento = int(input())
        if intento == numero:
            ayuda+=1
            print("Has acertado. Se han necesitado", ayuda, "intentos")
            break
        elif intento > numero:
            print("Demasiado grande")
            ayuda+=1
        else: # intento < numero
            print("Demasiado pequeño")
            ayuda+=1
intro()
