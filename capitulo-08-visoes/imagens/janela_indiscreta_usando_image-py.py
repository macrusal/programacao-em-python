import image


def cria_janela_indiscreta(nome, largura, altura):
    janela = image.ImageWin(largura, altura, nome)

    # Cria fundo manualmente
    imagem_fundo = image.EmptyImage(largura, altura)
    pixel_azul = image.Pixel(255, 0, 255)  # RGB para azul

    for x in range(largura):
        for y in range(altura):
            imagem_fundo.setPixel(x, y, pixel_azul)

    imagem_fundo.draw(janela)
    janela.exitOnClick()


if __name__ == '__main__':
    cria_janela_indiscreta('Janela Indiscreta', 320, 240)