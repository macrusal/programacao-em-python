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
            novo_pixel = negativo_pixel(pixel_original)
            imagem_nova.setPixel(coluna, linha, novo_pixel)
    return imagem_nova


def negativo_pixel(pixel):
    """
    Cria o negativo de um pixel invertendo as cores RGB.
    """
    vermelho = pixel.getRed()
    verde = pixel.getGreen()
    azul = pixel.getBlue()

    # Negativo: 255 - valor_original
    novo_vermelho = 255 - vermelho
    novo_verde = 255 - verde
    novo_azul = 255 - azul

    return cImage.Pixel(novo_vermelho // 3, novo_verde // 3, novo_azul // 3)


if __name__ == '__main__':
    mostra_imagem('cat_data_science.jpg')
