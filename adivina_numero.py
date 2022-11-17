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
        juega(0, 100, 0, numero_aleatorio(0, 100))
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
def numero_intento(minimo, maximo):
    while True:
        intento = input("Introduzca un número entre " + str(minimo) + " y " + str(maximo) + ": ")
        try:
            intento = int(intento)
        except:
            pass
        else:
            # Realizar la comparación
            if minimo <= intento <= maximo:
                return intento
def juega(minimo, maximo, ayuda, numero):
    print (numero)
    while True:
        intento = numero_intento(minimo, maximo)
        if intento == numero:
            ayuda+=1
            print ("Has acertado. Se han necesitado", ayuda, "intentos")
            victoria(ayuda)
            break
        elif intento < numero:
            print ("Demasiado pequeño")
            ayuda+=1
            if ayuda == 5:
                ayudaf(minimo, maximo, numero, ayuda)
            elif ayuda == 10:
                maximointentos(minimo, maximo, ayuda)
        elif intento > numero:
            print ("Demasiado grande")
            ayuda+=1
            if ayuda == 5:
                ayudaf(minimo, maximo, numero, ayuda)
            elif ayuda == 10:
                maximointentos(minimo, maximo, ayuda)
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
        juega(nuevomin, nuevomax, ayuda, numero)
    elif pregunta == "N" or pregunta == "n":
        juega()
    else:
        return ayudaf(minimo, maximo, numero, ayuda)
def maximointentos(minimo, maximo, ayuda):
    if ayuda == 10:
        print ("Has perdido. Alcanzaste el máximo numero de intentos:", ayuda)
        p = input("¿Quiere volver a jugar? (S/N): ")
        print (p)
        if p == "S" or p == "s":
            intro()
        elif p == "N" or p == "n":
            print ("Gracias por jugar")
            exit()
        else:
            return maximointentos(minimo, maximo, ayuda)
def victoria(ayuda):
    NomUsuario = input("Introduzca su nombre: ")
    print (NomUsuario)
    print (NomUsuario, ",¿Quiere que se guarde su puntuación? (S/N):")
    respuesta = input()
    if respuesta == "S" or respuesta == "s":
        print ("Su puntuación se ha guardado")
        listaGanadores = []
        listaGanadores.append(NomUsuario + " con " + str(ayuda) + " intentos")
        print (listaGanadores)
        print ("¿Quiere volver a jugar? (S/N): ")
        q = input()
        if q == "S" or q == "s":
            intro()
        elif q == "N" or q == "n":
            print ("Gracias por jugar")
            exit()
    elif respuesta == "N":
        print ("Su puntuación no se ha guardado")
        print("Gracias por jugar")
        intro()
    else:
        victoria()
#INTELIGENCIA ARTIFICIAL
intro()
