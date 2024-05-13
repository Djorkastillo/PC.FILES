import random
print("Semana No. 16: Ejercicio 1")
A=[]
for i in range(10):
    r=random.randint(1,100)
    A.append(r)

promedio=0
for num in A:
    promedio+=num
promedio=promedio/len(A)
print("Los valores aleatorios son: \n",A)
print("La cantidad de elementos es: ",len(A))
print("El promedio es: ",promedio)

sumapar=0
sumaimpar=0
for i in range(len(A)):
    if i %2==0:
        sumapar+=A[i]
    else:
        sumaimpar+=A[i]

print("La suma par es: ",sumapar)
print("La suma impar es: ",sumaimpar)

print("Semana No. 16: Ejercicio 2")

filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("Ingrese la cantidad de columnas: "))

B=[]
for i in range(filas):
    temporal=[]
    for j in range(columnas):
        r=random.randint(1,1001)
        temporal.append(r)
    B.append(temporal)
print(B)

contadorpares=0
contadorimpares=0
for fila in B:
    for numero in fila:
        if i%2==0:
            contadorpares=contadorpares+1
        else:
            contadorimpares=contadorimpares+1
print("La cantidad de numeros pares es: "+str(contadorpares))
print("La cantidad de numeros impares es: "+str(contadorimpares))

mayor=0
def NumMayor(B):
    mayor=B[0][0]
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j]>mayor:
                mayor=B[i][j]
    return mayor
print("El numero mayor es: " +str(NumMayor(B)))

menor=0
def NumMenor(B):
    menor=B[0][0]
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j]<menor:
                menor=B[i][j]
    return menor
print("El numero menor es: " +str(NumMenor(B)))
