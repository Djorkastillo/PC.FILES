#Donovan Castillo - 1302824
print("ACTIVIDAD NO.3")
print("Ejercicio 1: operaciones aritmeticas")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

total = num1+num2
diferencia = num1-num2
producto = num1*num2
divreal = num1/num2
divent = num1//num2
residuo = num1%num2
potencia = num1**num2

print(num1,"+",num2,"=",total)
print(num1,"-",num2,"="+str(diferencia))
print(num1,"x",num2,"=",producto)
print(num1,"/",num2,"=",divreal)
print(num1,"//",num2,"=",divent)
print(num1,"%",num2,"=",residuo)
print(num1,"^",num2,"=",potencia)
print()

print("Ejercicio 2: Operaciones booleanas")
igualdad = num1==num2
mayorque = num1>num2
menorque = num1<num2
distinto = num1!=num2

print(num1,"es igual a",num2,":",igualdad)
print(num1,"mayor que",num2,":",mayorque)
print(num1,"menor que",num2,":",menorque)
print(num1,"es distinto a",num2,":",distinto)
print()

print("Ejercicio 3: Jerarquia de operadores")
a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))
c = int(input("Ingrese el tercer valor: "))

i = a*b+c
ii = a*(b+c)
iii = a/(b+c)
iv = ((3*a) + (2*b))/(c**2)

print("a*b+c =",i)
print("a*(b+c) =",ii)
print("a/(b+c) =",iii)
print("((3*a) + (2*b))/(c**2) =",iv)

print()
print()

print("ACTIVIDAD NO.3")
num3 = int(input("Ingrese un tercer numero en metros:  "))
mi = num3/1.69
km = num3/1000
ft = num3*3.28
pg = num3*39.37

print("Millas:",mi)
print("Kilometros:",km)
print("Pies:",ft)
print("Pulgadas:",pg)
print()
num4 = int(input("Ingrese un cuarto numero en metros:  "))
yrds = num4*1.09
fts = num4*3.28
mtrs = num4*1

print("Yardas:",yrds)
print("Pies:",fts)
print("Metros:",mtrs)
