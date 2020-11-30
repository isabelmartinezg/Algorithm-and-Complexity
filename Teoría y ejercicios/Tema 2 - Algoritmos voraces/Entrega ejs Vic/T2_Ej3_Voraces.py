def mayor_menor(Lista):
    minimo = []
    maximo = []

    while (len(Lista) > 1):
        if (Lista[0] > Lista[1]):
            maximo.append(Lista[0])
            minimo.append(Lista[1])
            del(Lista[0])
            del(Lista[0])

        else:
            maximo.append(Lista[1])
            minimo.append(Lista[0])
            del(Lista[0])
            del(Lista[0])

        if (len(Lista) == 1):
            if(Lista[0]) > maximo[0]:
                maximo.append(Lista[0])
                del(Lista[0])

            else:
                minimo.append(Lista[0])
                del(Lista[0])

        maxM = maximo[0]
        for i in maximo:
            if (i > maxM):
                maxM = i

        minM = minimo [0]
        for i in minimo:
            if (i < minM):
                minM = i

    print("El valor MÍNIMO es: ", minM)
    print("El valor MÁXIMO es: ", maxM)

Lista = [2, 7, 15, 0, 200, 87, 151]
mayor_menor(Lista)
