import math
def Sumar(num1,num2):
    Total=num1+num2 #cambiar el signo para hacer diferentes operaciones
    return Total


def Restar(num1,num2):
    Total=num1-num2 #cambiar el signo para hacer diferentes operaciones
    return Total


def Multiplicar(num1,num2):
    Total=num1*num2 #cambiar el signo para hacer diferentes operaciones
    return Total


def Dividir(num1,num2):
    Total=num1/num2 #cambiar el signo para hacer diferentes operaciones
    return Total


def Raiz(num1):
    Total=math.sqrt(num1) #cambiar el signo para hacer diferentes operaciones
    return Total


def Potencia(num1,num2):
    Total=num1**num2 #cambiar el signo para hacer diferentes operaciones
    return Total

def Factorial(num):
    for i in range(1,num+1):
        if i==1:
            factorial=1
        else:
            factorial *=i
    return factorial

aceptado=True
while aceptado==True:
    print("Menu de Opciones")
    print("1.Sumar")
    print("2.Restar")
    print("3.Multiplicar")
    print("4.Division")
    print("5.Potencia")
    print("6.Raiz cuadrada")
    print("7.Factorial")
    opcion=int(input("Ingrese la opcion deseada\n"))
    if opcion<=0 or opcion>7:
        print("Numero no valido, intente de nuevo")
        aceptado = False
    
    else:
        if opcion==1:
            num1=int(input("Ingrese un primer numero: "))
            num2=int(input("Ingresar un segundo numero: "))
            print("La suma es :"+ str(Sumar(num1,num2)))

        if opcion==2:
            num1=int(input("Ingrese un primer numero: "))
            num2=int(input("Ingresar un segundo numero: "))
            print("La resta es :"+ str(Restar(num1,num2)))
        
        if opcion==3:
            num1=int(input("Ingrese un primer numero: "))
            num2=int(input("Ingresar un segundo numero: "))
            print("La multiplicar es :"+ str(Multiplicar(num1,num2)))

        if opcion==4:
            num1=int(input("Ingrese un primer numero: "))
            num2=int(input("Ingresar un segundo numero: "))
            if(num2!=0):
                print("La division es :"+ str(Dividir(num1,num2)))
            else:
                print("No se puede dividir dentro de cero")

        if opcion==5:
            num1=int(input("Ingrese un primer numero: "))
            num2=int(input("Ingresar un segundo numero: "))
            print("La potencia es :"+ str(Potencia(num1,num2)))

        if opcion==6:
            num1=int(input("Ingrese un primer numero: "))
            print("La raiz cuadrada es :"+ str(Raiz(num1)))

        if opcion==7:
            num1=int(input("Ingrese un primer numero: "))
            if num1>0:
                print("La factorial es :"+ str(Factorial(num1)))
            else:
                print("No se puede calcular")

        resp=input("Desea salir? (s/n)")
        if resp=="s" or resp=="si" or resp=="si":
            aceptado=False
