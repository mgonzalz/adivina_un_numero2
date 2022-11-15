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
    print (numero)
    ayuda = 0 #HACER PARA QUE SE REPITA LA FUNCION DE VARIABLE Y NO SE ACTUALICE SIEMPRE QUE SE REPITA A CERO
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
        elif intento > numero:
            print ("Demasiado grande")
            ayuda+=1
        elif intento < numero:
            print ("Demasiado pequeño")
            ayuda+=1
        else:
            return juega() #ARREGLAR QUE SI SE PONE LETRA U OTRA COSA QUE NO SEA NUMERO PERMITA INTENTARLO OTRA VEZ
def ayuda(minimo, maximo, ayuda):
    if ayuda == 5:
        print (input("¿Necesita ayuda? (S/N): "))
        if ayuda == "S":
            print ("El numero está entre", maximo -(maximo/2), "y", minimo -(minimo/2))
        elif ayuda == "N":
            juega(minimo, maximo, ayuda)
    else:
        juega(minimo, maximo)
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
