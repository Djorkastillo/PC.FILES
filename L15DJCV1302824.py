#Area de definicion de funciones
def menu():
    print("Elija una opcion: \na. Area de triangulo\nb. Area de cuadrado\nc. Area de rectangulo\nd. Area de circulo")
    opcion=input()
    return opcion
def obtenerareatriangulo(base,altura):
    area=(base*altura)/2
    return area
def obtenerareacuadrado(lado):
    area=(lado**2)
    return area
def obtenerarearectangulo(base,altura):
    area=(base*altura)
    return area
def obtenerareacirculo(radio):
    area=3.1416*(radio**2)
    return area
#Area de interaccion con el usuario
print("Semana No. 15 - Ejercicio 1\nActividad No.1")
print()
match(menu()):
    case "a":
       print("El area del trinagulo es: ", obtenerareatriangulo(float(input("Ingrese la base del triangulo: ")), float(input("Ingrese la altura del triangulo: "))))

    case "b":
       print("El area del cuadrado es: ", obtenerareacuadrado(float(input("Ingrese el lado del cuadrado: "))))

    case "c":
       print("El area del rectangulo es: ", obtenerarearectangulo(float(input("Ingrese la base del rectangulo: ")), float(input("Ingrese la altura del rectangulo: "))))

    case "d":
       print("El area del circulo es: ", round(obtenerareacirculo(float(input("Ingrese el radio del circulo: "))),2))

#Area de interaccion con el usuario
print("Semana No. 15 - Ejercicio 1\nActividad No.2")
print()
def menu2():
    print("Elija una opcion: \na. Sube\nb. Baja\nc. Izquierda\nd. Derecha\ne. Salir")
    opcion=input()
    return opcion

x=0
y=0
def moverhaciaarriba():
    global y
    y +=1

def moverhaciaabajo():
    global y
    y -=1

def moverhaciaizquierda():
    global x
    x -=1

def moverhaciaderecha():
    global x
    x +=1

while True:
    opcion = menu()
    match opcion:
        case "a":
            moverhaciaarriba()
        case "b":
            moverhaciaabajo()
        case "c":
            moverhaciaizquierda()
        case "d":
            moverhaciaderecha()
        case "e":
            print("Las coordenadas finales del personaje son: " + str(x) + "," + str(y))
            break
        case _:
            print("No sirve este dato. Ingrese algo razonable.")


