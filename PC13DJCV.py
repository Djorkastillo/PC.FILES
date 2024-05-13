import math
n = int(input("Ingrese la cantidad de numeros: "))

lista=[]

for i in range(n):
    valor = int(input("Ingrese un numero: "))
    lista.append(valor)
sumatoria=0
for i in lista:
    sumatoria= sumatoria+i
promedio=sumatoria/n
print("EL proimedio es "+ str(promedio))
numerador=0
for i in lista:
    numerador=(promedio-i)**2
desviacion=math.sqrt(numerador/n)
print("La desviacion estandar es "+ str(desviacion))
