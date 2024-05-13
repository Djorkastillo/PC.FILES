import math

print("Tercer Programa")
num1 = input("Ingrese el radio: ")
num1 = float(num1)

A = math.pi * (num1**2)
print(f"El area de la circunferencia es: {A: .2f}")
P = 2*math.pi*num1
print(f"El perimetro de la circunferencia es: {P: .2f}")

