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
def numero_aleatorio(minimo, maximo):
    import random
    numero = random.randint(minimo, maximo)
    return numero
def juega(minimo, maximo, ayuda):
    numero = numero_aleatorio(minimo, maximo)
    print (numero)
    while True:
        print ("Introduzca un numero entre", minimo, "y", maximo)
        intento = input()
        try:
            intento = int(intento)
        except:
            pass
        else:
            if minimo <= intento <= maximo:
                break
        if intento == numero:
            ayuda+=1
            print ("Has acertado. Se han necesitado", ayuda, "intentos")
            victoria(ayuda)
            break
        elif intento < numero:
            print ("El numero es mayor")
            ayuda+=1
            if ayuda == 5:
                ayudaf(minimo, maximo, numero, ayuda)
        elif intento > numero:
            print ("Demasiado grande")
            ayuda+=1
            if ayuda == 5:
                ayudaf(minimo, maximo, numero, ayuda)
        elif intento < numero:
            print ("Demasiado pequeño")
            ayuda+=1
        else:
            return True
def ayudaf(minimo, maximo, numero, ayuda):
    pregunta = input("¿Necesita ayuda? (S/N): ")
    print (pregunta)
    MIN = minimo
    MAX = maximo
    import random
    nuevomin = random.randint(MIN, numero)
    nuevomax = random.randint(numero, MAX)
    if pregunta == "S" or pregunta == "s":
        print ("El numero está se encuentra entre los siguientes valores:",nuevomin, ", ", nuevomax)
        juega(nuevomin, nuevomax, ayuda)
    elif pregunta == "N" or pregunta == "n":
        juega()
    else:
        return ayudaf(minimo, maximo, numero, ayuda)
def victoria(ayuda):
    NomUsuario = input("Introduzca su nombre: ")
    print (NomUsuario)
    print (NomUsuario, ",¿Quiere que se guarde su puntuación? (S/N):")
    respuesta = input()
    if respuesta == "S":
        Ganador = NomUsuario + " " + str(ayuda)
        list.append(Ganador)
        for Ganador in list:
            print ("Nombre: ", NomUsuario, "Intentos: ", ayuda)
        print ("Su puntuación se ha guardado")
    elif respuesta == "N":
        print ("Su puntuación no se ha guardado")
        intro()
    else:
        victoria()
#DETERMINAR UN N MAXIMO DE INTENTOS
#MOSTRAR LISTA DE PUNTUACIONES
#INTELIGENCIA ARTIFICIAL
intro()
