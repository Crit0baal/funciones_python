import os 
from functions import *
os.system("cls")


#crear lista
notas = []
while True:
    os.system("cls")
    print("1) agregar nota")
    print("2) mostrar notas")
    try:
        opcion = int(input("ingrese opcion\n"))
        if opcion == 1:
            os.system("cls")
            agregar_nota(notas)
        elif opcion == 2:
            os.system("cls")
            mostrar_notas(notas)
        else:
            print("opcion no existe")
    except:
        print("opcion debe ser un valor numerico entero")