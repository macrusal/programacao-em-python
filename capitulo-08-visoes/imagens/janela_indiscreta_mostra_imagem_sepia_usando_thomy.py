import cImage


def mostra_imagem(img_arquivo):
    imagem = cImage.FileImage(img_arquivo)
    imagem_nova = negativo_imagem(imagem)
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    janela = cImage.ImageWin('Janela de Imagem', 2 * imagem_nova.getWidth(), imagem_nova.getHeight())
    imagem.draw(janela)
    imagem_nova.setPosition(largura + 1, 0)
    imagem_nova.draw(janela)
    janela.exitOnClick()


def negativo_imagem(imagem):
    largura = imagem.getWidth()
    altura = imagem.getHeight()
    imagem_nova = cImage.EmptyImage(largura, altura)

    obter_matriz_3d_rgb(imagem_nova)

    for coluna in range(largura):
        for linha in range(altura):
            pixel_original = imagem.getPixel(coluna, linha)
            novo_pixel = sepia_pixel(pixel_original)
            imagem_nova.setPixel(coluna, linha, novo_pixel)
    return imagem_nova


def sepia_pixel(pixel):
    """
    Cria o sepia de um pixel invertendo as cores RGB.
    """
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()

    novo_vermelho = int(vermelho * 0.393 + verde * 0.769 + azul * 0.189)
    novo_verde = int(vermelho * 0.349 + verde * 0.686 + azul * 0.168)
    novo_azul = int(vermelho * 0.272 + verde * 0.534 + azul * 0.131)

    if novo_vermelho > 255:
        novo_vermelho = vermelho
    if novo_verde > 255:
        novo_verde = verde
    if novo_azul > 255:
        novo_azul = azul

    return cImage.Pixel(novo_vermelho, novo_verde, novo_azul)


if __name__ == '__main__':
    mostra_imagem('cat_data_science.jpg')
