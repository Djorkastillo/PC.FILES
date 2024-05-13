# MES EN ESPANOL A INGLES
try:
       print()
       print("Traductor de Español a Ingles")
       print()
       print("Instrucción: Ingresar solo carácteres ALFABÉTICOS, todo en mayúsculas.")
       mes = str(input("Ingrese el nombre de un mes: "))
       if mes == "ENERO":
               print("En ingles: JANUARY")
       else:
              if mes == "FEBRERO":
                     print("En ingles: FEBRUARY")
              elif mes == "MARZO":
                     print("En ingles: MARCH")
              elif mes == "ABRIL":
                     print("En ingles: APRIL")
              elif mes == "MAYO":
                     print("En ingles: MAY")
              elif mes == "JUNIO":
                     print("En ingles: JUNE")               
              elif mes == "JULIO":
               print("En ingles: JULY")
              elif mes == "AGOSTO":
               print("En ingles: AUGUST")  
              elif mes == "SEPTIEMBRE":
               print("En ingles: SEPTEMBER")  
              elif mes == "OCTUBRE":
               print("En ingles: OCTOBER")
              elif mes == "NOBIEMBRE":
               print("En ingles :NOBEMBER")
              elif mes == "DICIEMBRE":
               print("En ingles: DICEMBER")
              else:
                print()
                print("Error, siga las instrucciones.")   
                print()
except ValueError:
       print("SIGA LAS INSTRUCCIONES")
