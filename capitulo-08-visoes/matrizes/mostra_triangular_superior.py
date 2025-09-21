def mostra_tri_sup(matriz):
    """
    Matriz triangular, superior. Indexação pela posição
    """
    for pos_linha in range(len(matriz)):
        print(' '* 3 * pos_linha, end=' ')
        for pos_coluna in range(pos_linha, len(matriz[0])):
            print("%4d" % matriz[pos_linha][pos_coluna], end=' ')
        print()


if __name__ == '__main__':
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mostra_tri_sup(matriz)