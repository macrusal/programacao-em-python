import cImage


def mostra_imagem(img_arquivo):

    imagem = cImage.FileImage(img_arquivo)
    altura = imagem.getHeight()
    largura = imagem.getWidth()
    janela = cImage.ImageWin('Janela de Imagem', largura, altura)
    imagem.draw(janela)
    janela.exitOnClick()


def cria_janela_indiscreta(largura, altura):
    # Cria uma imagem azul
    imagem = cImage.EmptyImage(largura, altura)
    pixel_azul = cImage.Pixel(100, 0, 255)  # RGB para azul

    for x in range(largura):
        for y in range(altura):
            imagem.setPixel(x, y, pixel_azul)


if __name__ == '__main__':
    cria_janela_indiscreta(320, 240)
    mostra_imagem('cat_data_science.jpg')
