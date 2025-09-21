def mostra_por_linhas(matriz):
    """
    Indexação pela posição
    """
    for pos_linha in range(len(matriz)):
        for pos_coluna in range(len(matriz[0])):
            print("%5d" % matriz[pos_linha][pos_coluna], end=' ')
        print()


if __name__ == '__main__':
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mostra_por_linhas(matriz)