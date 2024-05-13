#Ejercicio Tulito
print()
tulito = int(input("Ingresar un numero: "))
speed =  int(input("Ingresar numero de salto: "))
tulito2 = int(input("Ingresar numero a empezar: "))
tulito3 = int(input("Ingresar numero a terminar: "))
print()
if tulito3<tulito2:
    print("Error, valor invalido")
    if tulito<0:
        print("Error, valor invalido")

for (i) in range(tulito2, tulito3, speed):
    print(str(tulito) + "x"+ str(i) + "="+ str(tulito*i))
print()
print("Con programacion las matematicas son mas simples :)")
print()

#Generar numero aleatorio
import random
secreto = random.randint(1,100)
ganador = False
turnos = 0
print()
nombre1=input("Ingrese nombre de jugador1: ")
nombre2=input("Ingrese nombre de jugador2: ")
while not ganador:
    ingresado = int(input("Jugador1 ingrese un numero (1-100): "))
    ingresado2 = int(input("Jugador2 ingrese un numero (1-100): "))
    turnos+=1
    if ingresado<1 or ingresado>100:
        print("Numero no valido")
    if ingresado == secreto:
        print(nombre1, "Gano el juego :3")
        print()
        ganador = True
    else:
        if ingresado2<1 or ingresado2>100:
            print("Numero no valido")
        if ingresado2 == secreto:
            print(nombre2, "Gano el juego :3")
            print()
            ganador = True
        if ingresado<secreto:
            print(nombre1,"El numero es mayor")
        else:
            print(nombre1,"El numero es menor")
        if ingresado2<secreto:
            print(nombre2,"El numero es mayor")
        else:
            print(nombre2,"El numero es menor")
print(nombre1,"lo intento " + str(turnos)+ " veces")
print(nombre2,"lo intento " + str(turnos)+ " veces")
print()

