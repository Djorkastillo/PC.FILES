#ACTIVIDAD NO.1
print("Semana No. 10: Ejercicio 1")
mes = int(input("Ingrese número de mes: "))
if mes<1 or mes>12:
    print("Error: El número a ingresar debe estar contenido entre 1 y 12")
else: 
    if mes == 1:
        print("MES: Enero")
    elif mes == 2:
        print("MES: Febrero")
    elif mes == 3:
        print("MES: Marzo")
    elif mes == 4:
        print("MES: Abril")
    elif mes == 5:
        print("MES: Mayo")
    elif mes == 6:
        print("MES: Junio")
    elif mes == 7:
        print("MES: Julio")
    elif mes == 8:
        print("MES: Agosto")
    elif mes == 9:
        print("MES: Septiembre")
    elif mes == 10:
        print("MES: Octubre")
    elif mes == 11:
        print("MES: Noviembre")
    elif mes == 12:
        print("MES: Diciembre")
print()
#ACTIVIDAD NO.2
print("Semana No. 10: Ejercicio 2") 
num1 = int(input("Ingrese un primer número: "))
num2 = int(input("Ingrese un segundo número: ")) 
num3 = int(input("Ingrese un tercer número: "))                                                    
if num1<0:
   print("Número Inválido")
elif num2<0:
    print("Número Inválido")
elif num2<0:
    print("Número Inválido")
if num1>num2:
    if num1>num3:
        print("El número mayor es:",num1)
    else:
        if num1==num3:
            print("Los números mayores son:",num1,"y",num3)
        else:
            print("El número mayor es:",num3)
else:
    if num1==num2:
        if num1>num3:
            print("Los números mayores son:",num1,"y",num2)
        else:
            if num1==num3:
                print("Los tres números son iguales")
            else:
                print("El número mayor es:",num3)
    else: 
        if num2>num3:
            print("El número mayor es:",num2)
        else:
            if num2==num3:
                print("Los números mayores son:",num2,"y",num3)
            else:
                print("El número mayor es:",num3)
print()
#ACTIVIDAD NO.3
print("Nombre: Dónovan Castillo")
print("Carnet: 1302824")
try:
    d=int(input("Ingresar día de nacimiento en números: "))
    m=int(input("ingresar mes de nacimiento en números: "))
    a=int(input("Ingresar año de nacimiento en números: "))
    match m:
        case 1:
            if d<=19:
                print("Su signo zodiacal es: Capricornio")
            else:
                print("Su signo zodiacal es: Acuario")
        case 2:
            if d<=18:
                print("Su signo zodiacal es: Acuario")
            else:
                print("Su signo zodiacal es: Piscis")
        case 3:
            if d<=20:
                print("Su signo zodiacal es: Piscis")
            else:
                print("Su signo zodiacal es: Aries") 
        case 4:
            if d<=19:
                print("Su signo zodiacal es: Aries")
            else:
                print("Su signo zodiacal es: Tauro")
        case 5:
            if d<=20:
                print("Su signo zodiacal es: Tauro")
            else:
                print("Su signo zodiacal es: Geminis")
        case 6:
            if d<=20:
                print("Su signo zodiacal es: Geminis")
            else:
                print("Su signo zodiacal es: Cancer")
        case 7:
            if d<=22:
                print("Su signo zodiacal es: Cancer")
            else:
                print("Su signo zodiacal es: Leo")
        case 8:
            if d<=22:
                print("Su signo zodiacal es: Leo")
            else:
                print("Su signo zodiacal es: Virgo")
        case 9:
            if d<=22:
                print("Su signo zodiacal es: Virgo")
            else:
                print("Su signo zodiacal es: Libra")
        case 10:
            if d<=22:
                print("Su signo zodiacal es: Libra")
            else:
                print("Su signo zodiacal es: Escorpio")
        case 11:
            if d<=21:
                print("Su signo zodiacal es: Escorpio")
            else:
                print("Su signo zodiacal es: Sagitario")
        case 12:
            if d<=21:
                print("Su signo zodiacal es: Sagitario")
            else:
                print("Su signo zodiacal es: Capricornio")
        case 13:
                print("numero no valido")
except ValueError:
                print("Valor no valido")
