#TAREA NO SIRVE
import math
print("MENU\nElija una opcion:\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Raiz\n6.Potencia\n7.Factorial")
accion=int(input("Ingrese el numero de la opcion seleccionada: "))

if accion=="1":
    def Sumar(num1,num2):
        Total=num1+num2 #cambiar el signo para hacer diferentes operaciones
        return Total

if accion=="2":
    def Restar(num1,num2):
        Total=num1-num2 #cambiar el signo para hacer diferentes operaciones
        return Total

if accion=="3":
    def Multiplicar(num1,num2):
        Total=num1*num2 #cambiar el signo para hacer diferentes operaciones
        return Total

if accion=="4":
    def Dividir(num1,num2):
        Total=num1/num2 #cambiar el signo para hacer diferentes operaciones
        return Total

if accion=="5":
    def Raiz(num1):
        Total=math.sqrt(num1) #cambiar el signo para hacer diferentes operaciones
        return Total

if accion=="6":
    def Potencia(num1,num2):
        Total=num1**num2 #cambiar el signo para hacer diferentes operaciones
        return Total

if accion=="7":
    def Factorial(num):
        for i in range(1,num+1):
            if i==1:
                factorial=1
            else:
                factorial *=i
        return factorial

numero1=int(input("Ingrese un primer numero: "))
numero2=int(input("Ingrese un segundo numero: "))

print("La suma es: "+ str(Sumar(numero1,numero2)))
print("La resta es: "+ str(Restar(numero1,numero2)))
print("La multiplicacion es: "+ str(Multiplicar(numero1,numero2)))
if numero2==0:
    print("No es posible dividir dentro de 0")
else:
    print("La division es: "+ str(Dividir(numero1,numero2)))
print("La raiz cuadrada es: "+ str(Raiz(numero1)))
print("La potencia es: "+ str(Potencia(numero1,numero2)))
print("La factorial es: "+ str(Factorial(numero1,numero2)))
