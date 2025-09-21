def soma_matrizes(mat1, mat2):
    """
    Soma duas matrizes da mesma dimensão
    """

    numero_linhas = len(mat1)
    numero_colunas = len(mat1[0])
    mat = cria_matriz(numero_linhas, numero_colunas, 0)

    for i in range(numero_linhas):
        for j in range(numero_colunas):
            mat[i][j] = mat1[i][j] + mat2[i][j]

    return mat


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
    matriz_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_b = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
    print(soma_matrizes(matriz_a, matriz_b))
