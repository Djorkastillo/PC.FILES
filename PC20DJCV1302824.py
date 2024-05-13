#matriz simple
matriz = [[1,2,3],[1,2,3],[1,2,3]]

for fila in matriz:
    for valor in fila:
        print(str(valor), end=" ")
    print()

#cualquier matriz
def crear_matriz(filas,columnas):
    matriz = []
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            valor=int(input(f"Ingrese las edades para[{i},{j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

f = int(input("Ingrese valor para filas: "))
c = int(input("Ingrese valor para columnas: "))
matriz = crear_matriz(f,c)
for fila in matriz:
    print(fila)

mayor=0
for i in matriz:
    if(i>mayor):
       mayor = i
print("La edad mayor es: " +str(mayor))
