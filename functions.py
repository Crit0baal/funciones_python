
#funcion encargada de agregar notas
#arg: lista de notas
def agregar_nota(lista):
    nota = 0.0
    while nota <= 0.0 or nota > 7.0:
        nota = float(input("ingrese nota\n"))
    lista.append(nota)
    print("nota guardada...")
   
#funcion encargada de mostrar notas 
#args: lista de notas
def mostrar_notas(lista):
    if len(lista) == 0:
        print("no existen notas")
    else:
        print("Listado de notas")
        for x in lista:
            print(x)