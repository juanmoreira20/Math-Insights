def eliminação(l1, l2, col, aux=0):
    fator = (l2[col]-aux) / l1[col]
    for i in range(len(l2)):
        l2[i] -= fator * l1[i]

def gauss_jordan(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matriz Singular")
        for j in range(i+1, len(a)):
            eliminação(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminação(a[i], a[j], i)
    for i in range(len(a)):
        eliminação(a[i], a[i], i, aux=1)
    return a

def inverter(a):
    if len(matriz) == len(matriz[0]):
        auxmat = []
        for _ in a:
            auxmat.append([])
        for i,l in enumerate(a):
            assert len(l) == len(a)
            auxmat[i].extend(l + [0]*i + [1] + [0]*(len(a)-i-1))
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
