
print("Cuarto Programa")
num1 = input("Ingresar tiempo 1: ")
num2 = input("Ingresar tiempo 2: ")
num3 = input("Ingresar tiempo 3: ")
num4 = input("Ingresar tiempo 4: ")

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
num4 = float(num4)

P1 = 100/num1
P2 = 100/num2
P3 = 100/num3
P4 = 100/num4

Promedio = (P1+P2+P3+P4)/4
print(f"El proedio de velocidad de los cuatro deportistas es: {Promedio: .2f} m/s")
