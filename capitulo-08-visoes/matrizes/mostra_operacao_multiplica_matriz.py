def multiplica_matrizes(mat1, mat2):
    """
    Multiplica duas matrizes i*k e k*j
    """

    numero_linhas = len(mat1)
    numero_colunas = len(mat1[0])
    numero_colunas_2 = len(mat2[0])
    mat_prod = cria_matriz(numero_linhas, numero_colunas_2, 0)

    for i in range(numero_linhas):
        for j in range(numero_colunas_2):
            val = 0
            for k in range(numero_colunas):
                val = val + mat1[i][k] * mat2[k][j]
            mat_prod[i][j] = val

    return mat_prod


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
    matriz_b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(multiplica_matrizes(matriz_a, matriz_b))
