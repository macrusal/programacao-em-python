import cImage


def obter_matriz_3d_rgb(imagem):
    """
    Retorna matriz 3D: matriz[linha][coluna] = [R, G, B]
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()

    matriz_3d = []
    for linha in range(altura):
        linha_pixels = []
        for coluna in range(largura):
            pixel = imagem.getPixel(coluna, linha)
            rgb_lista = [pixel.getRed(), pixel.getGreen(), pixel.getBlue()]
            linha_pixels.append(rgb_lista)
        matriz_3d.append(linha_pixels)

    return matriz_3d


def criar_imagem_de_matriz_3d(matriz_3d):
    """
    Cria uma imagem cImage a partir de uma matriz 3D RGB
    """
    altura = len(matriz_3d)
    largura = len(matriz_3d[0]) if altura > 0 else 0

    nova_imagem = cImage.EmptyImage(largura, altura)

    for linha in range(altura):
        for coluna in range(largura):
            r, g, b = matriz_3d[linha][coluna]
            pixel = cImage.Pixel(r, g, b)
            nova_imagem.setPixel(coluna, linha, pixel)

    return nova_imagem


def mostrar_info_matriz_3d(matriz_3d, nome="Matriz"):
    """
    Mostra informações sobre a matriz 3D
    """
    altura = len(matriz_3d)
    largura = len(matriz_3d[0]) if altura > 0 else 0

    print(f"\n=== {nome} ===")
    print(f"Dimensões: {altura} linhas x {largura} colunas")
    print(f"Formato: matriz[linha][coluna] = [R, G, B]")

    # Mostra amostra do canto superior esquerdo
    print("Amostra 3x3 (canto superior esquerdo):")
    for linha in range(min(3, altura)):
        linha_amostra = []
        for coluna in range(min(3, largura)):
            linha_amostra.append(matriz_3d[linha][coluna])
        print(f"  Linha {linha}: {linha_amostra}")


def mostra_imagem(img_arquivo):
    """
    Função principal que mostra imagem original e com efeito sepia
    Agora também extrai e exibe informações das matrizes 3D
    """
    print(f"Carregando arquivo: {img_arquivo}")
    imagem = cImage.FileImage(img_arquivo)

    # OBTER MATRIZ 3D DA IMAGEM ORIGINAL
    print("Extraindo matriz 3D da imagem original...")
    matriz_original = obter_matriz_3d_rgb(imagem)
    mostrar_info_matriz_3d(matriz_original, "Imagem Original")

    # Processa imagem (aplica efeito sepia)
    print("Aplicando efeito sepia...")
    imagem_nova = negativo_imagem(imagem)

    # OBTER MATRIZ 3D DA IMAGEM PROCESSADA
    print("Extraindo matriz 3D da imagem com sepia...")
    matriz_sepia = obter_matriz_3d_rgb(imagem_nova)
    mostrar_info_matriz_3d(matriz_sepia, "Imagem Sepia")

    # Compara alguns pixels
    comparar_pixels(matriz_original, matriz_sepia)

    # Exibe as imagens
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Janela de Imagem', 2 * largura, altura)
    imagem.draw(janela)
    imagem_nova.setPosition(largura + 1, 0)
    imagem_nova.draw(janela)
    janela.exitOnClick()

    return matriz_original, matriz_sepia


def negativo_imagem(imagem):
    """
    Aplica efeito sepia na imagem (renomeei de negativo_imagem para manter seu código)
    """
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    imagem_nova = cImage.EmptyImage(largura, altura)

    for coluna in range(largura):
        for linha in range(altura):
            pixel_original = imagem.getPixel(coluna, linha)
            novo_pixel = sepia_pixel(pixel_original)
            imagem_nova.setPixel(coluna, linha, novo_pixel)

    return imagem_nova


def negativo_imagem_usando_matriz_3d(imagem):
    """
    Versão alternativa que usa matriz 3D para aplicar o efeito sepia
    """
    print("Aplicando sepia usando matriz 3D...")

    # 1. Converte imagem para matriz 3D
    matriz_original = obter_matriz_3d_rgb(imagem)

    # 2. Aplica efeito sepia na matriz
    altura = len(matriz_original)
    largura = len(matriz_original[0])
    matriz_sepia = []

    for linha in range(altura):
        linha_sepia = []
        for coluna in range(largura):
            r, g, b = matriz_original[linha][coluna]

            # Calcula sepia
            novo_r = int(r * 0.393 + g * 0.769 + b * 0.189)
            novo_g = int(r * 0.349 + g * 0.686 + b * 0.168)
            novo_b = int(r * 0.272 + g * 0.534 + b * 0.131)

            # Limita valores
            novo_r = min(255, novo_r)
            novo_g = min(255, novo_g)
            novo_b = min(255, novo_b)

            linha_sepia.append([novo_r, novo_g, novo_b])
        matriz_sepia.append(linha_sepia)

    # 3. Converte matriz 3D de volta para imagem
    imagem_sepia = criar_imagem_de_matriz_3d(matriz_sepia)

    return imagem_sepia, matriz_sepia


def comparar_pixels(matriz_original, matriz_sepia):
    """
    Compara alguns pixels entre original e sepia
    """
    print("\n=== COMPARAÇÃO DE PIXELS ===")

    altura = min(len(matriz_original), 3)
    largura = min(len(matriz_original[0]), 3)

    for linha in range(altura):
        for coluna in range(largura):
            orig = matriz_original[linha][coluna]
            sepia = matriz_sepia[linha][coluna]
            print(f"Pixel ({linha},{coluna}): {orig} -> {sepia}")


def sepia_pixel(pixel):
    """
    Aplica efeito sepia em um pixel
    """
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()

    novo_vermelho = int(vermelho * 0.393 + verde * 0.769 + azul * 0.189)
    novo_verde = int(vermelho * 0.349 + verde * 0.686 + azul * 0.168)
    novo_azul = int(vermelho * 0.272 + verde * 0.534 + azul * 0.131)

    # Corrigido: limita a 255 em vez de reverter para valor original
    novo_vermelho = min(255, novo_vermelho)
    novo_verde = min(255, novo_verde)
    novo_azul = min(255, novo_azul)

    return cImage.Pixel(novo_vermelho, novo_verde, novo_azul)


def exemplo_manipulacao_matriz():
    """
    Exemplo adicional de como manipular a matriz 3D
    """
    try:
        print("\n=== EXEMPLO DE MANIPULAÇÃO DE MATRIZ 3D ===")

        # Carrega imagem
        imagem = cImage.FileImage('cat_data_science.jpg')

        # Obtém matriz 3D
        matriz_3d = obter_matriz_3d_rgb(imagem)

        print(f"Matriz obtida: {len(matriz_3d)}x{len(matriz_3d[0])} pixels")

        # Exemplos de acesso
        print("\nExemplos de acesso:")
        pixel_00 = matriz_3d[0][0]
        print(f"Pixel (0,0): {pixel_00}")
        print(f"  Vermelho: {pixel_00[0]}")
        print(f"  Verde: {pixel_00[1]}")
        print(f"  Azul: {pixel_00[2]}")

        # Modifica um pixel
        matriz_3d[0][0] = [255, 0, 0]  # Torna vermelho
        print(f"Pixel (0,0) modificado para: {matriz_3d[0][0]}")

        # Converte de volta para imagem
        imagem_modificada = criar_imagem_de_matriz_3d(matriz_3d)
        print("Imagem recriada a partir da matriz 3D modificada")

        return matriz_3d

    except FileNotFoundError:
        print("Arquivo 'cat_data_science.jpg' não encontrado")
        return None


if __name__ == '__main__':
    # Executa programa principal
    try:
        matriz_orig, matriz_sepia = mostra_imagem('cat_data_science.jpg')

        # Exemplo adicional de manipulação
        exemplo_manipulacao_matriz()

        print("\n=== COMO USAR AS MATRIZES 3D ===")
        print("1. matriz_3d = obter_matriz_3d_rgb(imagem)")
        print("2. pixel = matriz_3d[linha][coluna]  # [R, G, B]")
        print("3. r, g, b = matriz_3d[linha][coluna]")
        print("4. matriz_3d[linha][coluna] = [novo_r, novo_g, novo_b]")
        print("5. nova_imagem = criar_imagem_de_matriz_3d(matriz_3d)")

    except FileNotFoundError:
        print("Arquivo 'cat_data_science.jpg' não encontrado.")
        print("Coloque o arquivo na mesma pasta do script.")
    except Exception as e:
        print(f"Erro: {e}")