def agregar_notas(lista):
    try:
        nota = 0
        while nota <=0:
            nota = float(input("ingrese nota \n"))
        lista.append(nota)
        print("la nota esta wena")
    except:
        print("debe ser numero ")