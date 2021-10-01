# Programa Pago de Bono

#1: Ingreso de Datos por el Usuario:
bono_general=float(input("Ingrese el valor del Bono General:"))
bono_eficiencia=float(input("Ingrese el valor del Bono de Eficiencia:"))

#2: Leer archivo
print("")
lista=[]
with open("creando el fichero nomina.txt","r",encoding = "utf-8") as nomina:
    nomina = nomina.readlines()
    for lineas in nomina:
        lista.append(lineas.split("\n"))

lista = (lista[1:]) 
for j in lista:
    print(j)


