def Escalar (listaShrek):
    coste = 0
    listaShrek.sort()

    for i in range(len(listaShrek)-1):
        suma = listaShrek[0] + listaShrek[1]
        coste = coste + suma

        del(listaShrek[0])
        del(listaShrek[0])

        listaShrek.insert(busquedaBinaria(listaShrek, suma), suma)

        print ("El coste es:", coste)

    return coste


def busquedaBinaria(lista, item):
    if len(lista) == 0:
        return 0
    else:
        puntoMedio = len(lista)//2
        if lista[puntoMedio-1] < item and lista[puntoMedio] > item:
            return puntoMedio
        else:
            if item < lista[puntoMedio]:
                return busquedaBinaria(lista[:puntoMedio], item)
            else:
                return busquedaBinaria(lista[puntoMedio+1:], item)+puntoMedio+1


ListaShrek = [25, 60, 1, 8, 6, 9, 27, 49, 62, 150, 200]
print("El coste final es:", Escalar(ListaShrek))
