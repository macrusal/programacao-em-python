def cria_matriz_c_lista_por_compreesao(n, m, val):
    """
    Cria matriz nXm sendo que todos os elementos são iguais a val
    """

    mat = [[val for x in range(m)] for y in range(n)]
    return mat


def cria_matriz_d_lista_por_operador_de_reprticao(n, m, val):
    """
    Cria matriz nXm sendo que todos os elementos são iguais a val
    """

    mat = [[val] * m] * n
    return mat


if __name__ == '__main__':
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(cria_matriz_c_lista_por_compreesao(1, 1, matriz))
    print()
    print(cria_matriz_d_lista_por_operador_de_reprticao(4, 4, matriz))