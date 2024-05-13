cant=int(input("Cantidad de datos a ingresar: "))
lista=[]
cantidad=0
while cantidad<cant:
    datos=int(input("Ingrese los datos: "))
    if(datos>0):
        lista.append(datos)
        cantidad=cantidad+1
    else:
        print("N'umero no valido, intentelo de nuevo")

mayor=0
for i in lista:
    if(i>mayor):
       mayor = i
print("El valor mayor es: " +str(mayor))
