def mostra_por_colunas(matriz):
    """
    Indexação pela posição
    """
    for pos_coluna in range(len(matriz[0])):
        for pos_linha in range(len(matriz)):
            print("%3d" % matriz[pos_linha][pos_coluna], end=' ')
        print()


if __name__ == '__main__':
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mostra_por_colunas(matriz)