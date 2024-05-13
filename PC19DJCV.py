#Cuantas edades, cual es la edad que le interesa, Ingrese edad, cuantos ingreso mayores a la erdad que le intertesa.
edad=int(input("Cual es la edad que le interesa: "))
numed=int(input("Cuantas edades desea ingresar: "))
lista=[]
cantidad=0
while cantidad<numed:
    edades=int(input("Ingrese las edades: "))
    if(edades>0):
        lista.append(edades)
        cantidad=cantidad+1
    else:
        print("Numero no valido, intentelo de nuevo")
i=0
r=0
for i in lista:
    if(i>edad):
        r+=1
print("Las edades que le interesan son: " +str(r))   
