def eliminação(l1, l2, col, aux=0):
    fator = (l2[col]-aux) / l1[col]
    for i in range(len(l2)):
        l2[i] -= fator * l1[i]

def gauss_jordan(matriz):
    for i in range(len(matriz)):
        if matriz[i][i] == 0:
            for j in range(i+1, len(matriz)):
                if matriz[i][j] != 0:
                    matriz[i], matriz[j] = matriz[j], matriz[i]
                    break
            else:
                raise ValueError("Matriz Singular")
        for j in range(i+1, len(matriz)):
            eliminação(matriz[i], matriz[j], i)
    for i in range(len(matriz)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminação(matriz[i], matriz[j], i)
    for i in range(len(matriz)):
        eliminação(matriz[i], matriz[i], i, aux=1)
    return matriz

def inverter(matriz):
    if len(matriz) == len(matriz[0]):
        auxmat = []
        for _ in matriz:
            auxmat.append([])
        for i,l in enumerate(matriz):
            assert len(l) == len(matriz)
            auxmat[i].extend(l + [0]*i + [1] + [0]*(len(matriz)-i-1))
        gauss_jordan(auxmat)
        inv = []
        for i in range(len(auxmat)):
            inv.append(auxmat[i][len(auxmat[i])//2:])
        return inv
    else:
        print("matriz não é nxn")
        exit()


def criar_matriz(matriz):
    L = int(input("Insira número de linhas: "))
    C = int(input("Insira número de colunas: "))
    print("Insira os elementos linha por linha")
    for i in range(L):
        a = []

        for j in range(C):
            a.append(int(input()))
        matriz.append(a)
    return matriz
def printar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end = " ")
        print()

matriz = []
matriz = criar_matriz(matriz)
matriz = inverter(matriz)
printar_matriz(matriz)
