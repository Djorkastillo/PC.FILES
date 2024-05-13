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
numero1=int(input("Ingrese un numero: "))
numero2=int(input("Ingrese un numero: "))

print("La suma es: "+ str(Sumar(numero1,numero2)))
print("La resta es: "+ str(Restar(numero1,numero2)))
print("La multiplicacion es: "+ str(Multiplicar(numero1,numero2)))
if numero2==0:
    print("No es posible dividir dentro de 0")
else:
    print("La division es: "+ str(Dividir(numero1,numero2)))

