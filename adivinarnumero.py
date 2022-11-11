#Elegir número
numero = int(input("Adivine el numero entre el 0 y el 99: "))
#Elección numero al azar
import random
numeroal = random.randint(0, 100)
numeroal = int(numeroal)
#Variable intentos
intentos = 0
#Intento
while True:
    if numero == numeroal:
        print("¡Has acertado! Se han necesitado", intentos ,"intentos")
        break
    elif numero < numeroal:
        print("Demasiado pequeño")
        numero = int(input("Adivine el numero entre el 0 y el 99: "))
        intentos+=1
    elif numero > numeroal:
        print("Demasiado grande")
        numero = int(input("Adivine el numero entre el 0 y el 99: "))
        intentos+=1
#Al utilizar "intentos+=1": Comando que consigue que cada vez que se ejecute el bucle, le  sume 1 a la variable "intentos"
