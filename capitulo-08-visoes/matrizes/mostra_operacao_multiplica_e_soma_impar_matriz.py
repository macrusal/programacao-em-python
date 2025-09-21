def multiplica_matrizes(mat, val):
    """
    Multiplica por 'val' os elementos das colunas de índice ímpar (2ª, 4ª, 6ª... colunas) de cada matriz.
    """

    numero_linhas = len(mat)
    numero_colunas = len(mat[0])

    for linha in range(numero_linhas):
        for coluna in range(1, numero_colunas, 2):
            mat[linha][coluna] *= val

    return mat


if __name__ == '__main__':
    matriz_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(multiplica_matrizes(matriz_a, 2))
