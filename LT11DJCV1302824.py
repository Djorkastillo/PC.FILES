#ACTIVIDAD NO.1
print("Semana No. 11: Ejercicio 1")
n = 0
while n<=0:
    n = int(input("Ingrese un numero mayor que 0: "))
    if n<=0:
        print("Numero invalido")
        print()
#El valor n ha sido leido

A=0
B=1
C=0
i=2
resultado=""
resultado = str(A)
if n>1:
    resultado +=(", "+str(B))
    while i<n:
        C=A+B
        resultado +=(", "+ str(C))
        A=B
        B=C
        i=i+1
    print(resultado)
else:
    print(resultado)
print()
#ACTIVIDAD NO.2
print("DONOVAN CASTILLO")
print("1302824")
print("Ejercicio a")
N = 0
while N<=0:
    N = int(input("Ingrese un numero mayor que 0: "))
    if N<=0:
        print("Numero invalido")
        print()
contador=1
sumatoria = 0
while contador<=N:
    sumatoria+=(1/contador)
    contador+=1
print(sumatoria)
print()
print("Ejercicio b")
N = 0
while N<=0:
    N = int(input("Ingrese un numero mayor que 0: "))
    if N<=0:
        print("Numero invalido")
        print()
contador=1
sumatoria = 0
while contador<=N:
    sumatoria+=(1/2**contador)
    contador+=1
print(sumatoria)
print()
print("Ejercicio c")
x = int(input("Ingrese un numero x: "))
a = int(input("Ingrese un numero a: "))
n1 = int(input("Ingrese un numero mayor que 0: "))
if n1<=0:
    print("Numero invalido")
    print()
k=0
sumatoria = 0
while k==0:
    sumatoria+=((x**k)*(a**(n1-1)))
    k+=1
print(sumatoria)

  


