import bubble_sort as DC
lista = []
while True:
    while True:
        try:
            e = int(input("Introducir elemento de lista a ordenar: "))
            break
        except:
            print("El dato introducido no es un número que sea válido")

    if (e == -9999):
        break
    lista.append(e)