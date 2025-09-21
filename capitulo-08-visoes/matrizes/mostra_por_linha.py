def mostra_por_linhas(matriz):
    """
    Indexação pelo conteúdo
    """
    for linha in matriz:
        for coluna in linha:
            print("%5d" % coluna, end=' ')
        print()


if __name__ == '__main__':
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mostra_por_linhas(matriz)