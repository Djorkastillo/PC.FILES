#FACTORIAL
def Factorial(num):
    for i in range(1,num+1):
        if i==1:
            factorial=1
        else:
            factorial *=i
    return factorial

num1=int(input("Ingrese un numero: "))
print("La multiplicacion es: "+ str(Factorial(num1)))

