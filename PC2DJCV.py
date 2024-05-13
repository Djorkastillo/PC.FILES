print("Segundo Programa")
num1 = input("Ingrese temperatura en Farenheit: ")
num1 = float(num1)

c = (num1 - 32)/1.8

print("La temperatura en celcius es: ""{0: .2f}".format(c))
print(f"La temperatura en celcius es: {c: .2f}")