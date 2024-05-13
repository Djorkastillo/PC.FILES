#4 Numero Par o Impar
try:
    num = int(input("Ingrese un numero: "))

    if num%2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")
except ValueError:
    print("Porfavor ingrese un numero valido")
