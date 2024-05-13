print("PROBLEMA NO.1")

monto = int(input("Ingrese un monto de carga: "))
descuento=0

if(monto<0):
    print("Error, monto no valido")
else:
    if(monto<=400):
        descuento=0
    elif 400< monto<=1000:
        descuento = 0.07
    elif 1000< monto<=5000:
        descuento = 0.1
    elif 5000< monto<=15000:
        descuento = 0.15
    else:
        descuento = 0,25

codigo = input("Tiene un codigo de descuento (s/n): ")
if(codigo=="si") or codigo=="si" or codigo =="s":
    descuento = descuento+0.05

monto = monto*(1-descuento)
print("El precio final es " + str(monto))
print("Se le aplico descuento de: ", str(descuento))

print()
print("PROBLEMA NO.2")
print("Ingrese el tipo de vehiculo: ")
TipoEnvio = int(input("1. Motocicleta, 2. Vehiculo: "))
CostoVariable=0

if TipoEnvio!= 1 and TipoEnvio!= 2:
    print("Error, tipo de envio no valido")
else:
    km = int(input("Ingrese el numero de kilometros a recorrer: "))
    if(km<0):
        print("Error, distancia no valida")
    else:
        if(TipoEnvio==1):
            CostoFijo= 10
            if(km<5):
                CostoVariable=km*3
            elif(km<10):
                CostoVariable=km*2.50
            else:
                CostoVariable=km*2
        if(TipoEnvio==2):
            CostoFijo= 20
            if(km<5):
                CostoVariable=km*6
            elif(km<10):
                CostoVariable=km*5
            else:
                CostoVariable=km*4
    CostoTotal = CostoFijo+CostoVariable
    print("El total de envio en quetzaleses de: ",CostoTotal)