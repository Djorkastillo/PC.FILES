#Sumatoria de divisores
num1=int(input("Ingrese un primer numero: "))
num2=int(input("Ingrese un segundo numero: "))

if num1<=0:
    print("Error, el numero debe ser positivo")
else:
    suma1=0
    for x in range (1,num1):
        if num1%x==0:
            suma1+=x
    if suma1 == num1:
        print("El numero es perfecto")
    else:
        print("El numero no es perfecto")
if num2<=0:
    print("Error, el numero debe ser positivo")
else:
    suma2=0
    for x in range (1,num1):
        if num2%x==0:
            suma2+=x
    if suma2 == num2:
        print("El numero es perfecto")
    else:
        print("El numero no es perfecto")
if suma2==num1 or suma1==num2:
    print("Los numeros son amigos")
else:
    print("Los numeros son enemigos")


