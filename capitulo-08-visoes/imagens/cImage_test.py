import cImage

def cria_janela(nome, largura, altura):
    janela = cImage.ImageWin(nome, largura, altura)
    janela.exitOnClick()

if __name__ == '__main__':
    cria_janela('Janela Indiscreta', 320, 240)