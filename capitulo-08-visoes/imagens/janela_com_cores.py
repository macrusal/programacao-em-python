import cImage


def cria_janela_indiscreta(nome, largura, altura):
    janela = cImage.ImageWin(nome, largura, altura)

    # Cria uma imagem azul
    imagem = cImage.EmptyImage(largura, altura)
    pixel_azul = cImage.Pixel(0, 0, 255)  # RGB para azul

    for x in range(largura):
        for y in range(altura):
            imagem.setPixel(x, y, pixel_azul)

    imagem.draw(janela)
    janela.exitOnClick()


if __name__ == '__main__':
    cria_janela_indiscreta('Janela Indiscreta', 320, 240)
