import bubble_sort as DC
while True:
    lista = []
    fin = False
    while True:
        while True:
            e = input("Introducir elemento de lista a ordenar: ")
            if e == "fin":
                fin = True
                break
            try:
                e = int(e)
                break
            except:
                print("El dato introducido no es un número que sea válido")
        if fin:
            break
        if (e == -9999):
            break
        lista.append(e)
    if fin:
        break
    lo = DC.BubbleSort(lista)
    print("Lista ordenada: ", lo.sorted_list)
