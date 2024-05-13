print("Determinar numeros primos")
print()
num1=int(input("Ingrese un numero: "))
cont=0
if (num1<=0):
    print("Error numero no valido")
else:
    for i in range(1, num1+1):
        if(num1%i==0):
            cont=cont+1
    if cont==2 or cont==1:
        print("El numero es primo")
    else:
        print("El numero no es primo")
