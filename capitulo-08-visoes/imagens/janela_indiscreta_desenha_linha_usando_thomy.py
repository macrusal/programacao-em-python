import cImage


def desenha_linha(imagem):
    altura = imagem.getHeight()
    largura = imagem.getWidth()
    # janela = cImage.ImageWin('Janela de Imagem', largura, altura)
    pix = cImage.Pixel(255, 0, 0)
    for coluna in range(largura):
        imagem.setPixel(coluna, altura // 2, pix)
    # imagem.draw(janela)
    # janela.exitOnClick()


def cria_janela_indiscreta(nome, largura, altura):
    janela = cImage.ImageWin(nome, largura, altura)

    # Cria uma imagem azul
    imagem = cImage.EmptyImage(largura, altura)
    pixel_azul = cImage.Pixel(100, 0, 255)  # RGB para azul

    for x in range(largura):
        for y in range(altura):
            imagem.setPixel(x, y, pixel_azul)

    desenha_linha(imagem)
    imagem.draw(janela)
    janela.exitOnClick()


if __name__ == '__main__':
    cria_janela_indiscreta('Janela Indiscreta', 320, 240)