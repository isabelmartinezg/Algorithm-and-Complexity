import math

def AlgoritmoPrim(matrixPrim):
    distanciaMin = [0]
    masProximo = [0]
    T = []
    conocidos = []

    for i in range (1, len (matrixPrim)):
        masProximo.append(0)
        distanciaMin.append(matrixPrim[i][0])

    for i in range(len(matrixPrim) - 1):
        min = math.inf

        for j in range (1, len(matrixPrim)):
            if (0 <= distanciaMin[j] and distanciaMin[j] < min and j not in conocidos):
                min = distanciaMin[j]
                k = j

        T.append([masProximo[k]+1, k+1])
        conocidos.append(k)

        for j in range (1, len(matrixPrim)):
            if matrixPrim[j][k] < distanciaMin[j]:
                distanciaMin[j] = matrixPrim[j][k]
                masProximo[j] = k

    return T

w = math.inf

matrix = [[0, w, 4, w, 5, 1, w],
          [w, 0, 3, 6, 2, w, w],
          [4, 3, 0, 5, w, w, 1],
          [w, 6, 5, 0, 9, w, 7],
          [5, 2, w, 9, 0, w, 5],
          [1, w, w, w, w, 0, 3],
          [w, w, 1, 7, 5, 3, 0]]

print(AlgoritmoPrim(matrix))
