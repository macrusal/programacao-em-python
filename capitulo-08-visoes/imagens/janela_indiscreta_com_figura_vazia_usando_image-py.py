import image


def cria_imagem_vazia(largura, altura):
    """
    Cria uma imagem vazia (transparente/preta)
    """
    imagem = image.EmptyImage(largura, altura)
    return imagem


def cria_imagem_colorida(largura, altura, r=255, g=255, b=255):
    """
    Cria uma imagem preenchida com uma cor específica
    """
    # imagem = image.EmptyImage(largura, altura)
    imagem = cria_imagem_vazia(largura, altura)
    cria_imagem_posicao(altura, imagem, largura)
    pixel_cor = image.Pixel(r, g, b)

    # Preenche toda a imagem com a cor
    for x in range(largura):
        for y in range(altura):
            imagem.setPixel(x, y, pixel_cor)

    return imagem


def cria_imagem_posicao(altura, imagem, largura):
    imagem.setPosition(largura / 2, altura / 2)


def mostra_imagem_simples(imagem):
    """
    Exibe uma imagem em uma janela
    """
    # CORREÇÃO 1: Métodos corretos (minúsculas)
    largura = imagem.getWidth()  # era GetWidth()
    altura = imagem.getHeight()  # era GetHeight()

    # Cria janela com o tamanho da imagem (ou 2x se quiser maior)
    janela = image.ImageWin(2*largura, 2*altura, 'Imagem')

    # CORREÇÃO 2: Primeiro desenha a imagem, depois aguarda clique
    imagem.draw(janela)
    janela.exitOnClick()


if __name__ == '__main__':
    # imagem = cria_imagem_vazia(320, 240)  # Guarda o retorno
    imagem = cria_imagem_colorida(320, 240, 255, 120, 30)  # Guarda o retorno
    mostra_imagem_simples(imagem)