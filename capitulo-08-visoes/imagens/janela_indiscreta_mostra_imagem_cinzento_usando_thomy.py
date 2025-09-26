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

    for coluna in range(largura):
        for linha in range(altura):
            pixel_original = imagem.getPixel(coluna, linha)
            novo_pixel = cinzento_pixel(pixel_original)
            imagem_nova.setPixel(coluna, linha, novo_pixel)
    return imagem_nova


def cinzento_pixel(pixel):
    """
    Cria o cinzento de um pixel invertendo as cores RGB.
    """
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()

    # Cinzento
    int_media = int(0.299*vermelho + 0.587*verde + 0.114*azul) // 3

    return cImage.Pixel(int_media, int_media, int_media)


if __name__ == '__main__':
    mostra_imagem('cat_data_science.jpg')
