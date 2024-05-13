#Actividad No.1
print("Semana No. 12: Ejercicio 1”")
print()
opcion = (input("Entre estas opciones:\n""a. Sumatoria \nb. Factorial \nc. Tablas de Multiplicar \nd. Número perfecto\n¿Cúal desea calcular?: "))
match opcion:
    case "a":
        n=0
        while(n<=0):
            n=int(input("Ingrese un entero positivo: "))
            if n<=0:
                print("El numero ingresado debe de ser mayor que cero")
        sumatoria=0
        for cont in range(1,n+1):
            sumatoria+=cont
        print("La sumatoria es: ",sumatoria)
    case _:
        print("Ingrese una opcion valida")

match opcion:
    case "b":
        n=0
        while(n<=0):
            n=int(input("Ingrese un entero positivo: "))
            if n<=0:
                print("El numero ingresado debe de ser mayor que cero")
        factorial=1
        for cont in range(1,n+1):
            factorial*=cont
        print("La factorial es: ",factorial)
    case _:
        print("Ingrese una opcion valida")

match opcion:
    case "c":
        for i in range(1,11):
            for j in range(1,11):
                print(i*j," ",end='')
            print()
    case _:
        print("Ingrese una opcion valida")

match opcion:
    case "d":
        n=0
        while(n<=0):
            n=int(input("Ingrese un entero positivo: "))
            if n<=0:
                print("El numero ingresado debe de ser mayor que cero")
        sumatoria=0
        for factor in (1,n):
            if n%factor==0: 
                sumatoria+=factor
        if sumatoria==n:
            print("El numero es perfecto")  
        else:
            print("El numero no es perfecto")
    case _:
        print("Ingrese una opcion valida")


