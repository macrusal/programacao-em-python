def cria_matriz(n, m, val):
    """
    Cria matriz nXm sendo que todos os elementos são iguais a val
    """

    mat = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(val)
        mat.append(linha)
    return mat


if __name__ == '__main__':
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(cria_matriz(2, 2, matriz))