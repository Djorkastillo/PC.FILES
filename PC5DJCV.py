#Mayor de edad?
edad = int(input("Ingrese una edad: "))


if edad<0 or edad >120:
    print("Edad no valida")
else:
    if edad>=18:
        print("La persona es mayor de edad")
    else:
        print("La persona es menor de edad")
print()

#Nota Aprobada
nota = int(input("Ingrese una nota: "))

if nota<0 or nota>100:
    print("Nota no valida")
else:
    if nota<65:
        print("Reprobado")
    else:
        print("Aprobado")
print()

#Rango de Notas
notas = int(input("Ingrese su nota: "))
if notas<0 or notas>100:
    print("Nota no valida")
else:
    if 0<notas<20:
        print("Metase a la Facultad de Ciencias Economicas y Empresiarales")
    else:
        if 21<notas<40:
            print("Metase a la Facultad de Humanidades")
        else:
            if 41<notas<60:
                print("Metase a la Facultad de Arquitectura y Diseño")
            else:
                if 61<notas<80:
                    print("Metase a la Facultad de Ciencias de la Salud")
                else:
                    if 81<notas<100:
                        print("Metase a la Facultad de Ingenieria")
print()
