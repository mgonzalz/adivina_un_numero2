def intro():
    print ("ADIVINE EL NUMERO")
    print ("***" * 10)
    print ("1. Nivel Simple (0-100)")
    print ("2. Nivel Intermedio (0-1000)")
    print ("3. Nivel Avanzado (0-1.000.000)")
    print ("4. Nivel Experto (0 y 1.000.000.000.000)")
    print ("5. Salir")
    nivel = input("Introduzca el nivel de dificultad: ")
    ayuda = 0
    if nivel == "1":
        juega(0, 100, 0)
    elif nivel == "2":
        juega(0, 1000, 0)
    elif nivel == "3":
        juega(0, 1000000, 0)
    elif nivel == "4":
        juega(0, 1000000000000, 0)
    elif nivel == "5":
        print("Gracias por jugar")
        exit()
    else:
        intro()
def juega(minimo, maximo, ayuda):
    import random
    numero = random.randint(minimo, maximo)
    print (numero)
    while True:
        print ("Introduzca un numero entre", minimo, "y", maximo)
        intento = int(input())
        if intento == numero:
            ayuda+=1
            print ("Has acertado. Se han necesitado", ayuda, "intentos")
            victoria()
            break
        elif intento < numero:
            print ("El numero es mayor")
            ayuda+=1
            if ayuda == 5:
                ayudaf(minimo, maximo, numero)
        elif intento > numero:
            print ("Demasiado grande")
            ayuda+=1
            if ayuda == 5:
                ayudaf(minimo, maximo, numero)
        elif intento < numero:
            print ("Demasiado pequeño")
            ayuda+=1
        elif intento > maximo or intento < minimo:
            return True
        else:
            return
def ayudaf(minimo, maximo, numero):
    pregunta = input("¿Necesita ayuda? (S/N): ")
    print (pregunta)
    MIN = minimo
    MAX = maximo
    import random
    nuevomin = random.randint(MIN, numero)
    nuevomax = random.randint(numero, MAX)
    if pregunta == "S" or pregunta == "s":
        print ("El numero está entre",nuevomin, "y", nuevomax)
        juega(nuevomin, nuevomax, 0)
    elif pregunta == "N" or pregunta == "n":
        juega()
    else:
        ayudaf()
def victoria():
    NomUsuario = input("Introduzca su nombre: ")
    print (NomUsuario)
    print (NomUsuario, input(",¿Quiere que se guarde su puntuación? (S/N):"))
    if NomUsuario == "S":
        print ("Su puntuación se ha guardado")
        lista.append(NomUsuario + " " + ayuda)
        print (lend(lista))     #ARREGLAR LA LISTA
    elif NomUsuario == "N":
        print ("Su puntuación no se ha guardado")
        intro()

intro()
