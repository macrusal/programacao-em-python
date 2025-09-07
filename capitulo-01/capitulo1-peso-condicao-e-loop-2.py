# definindo funções
def peso_altura_genero(param_range):
    for i in range(param_range):

        param_altura = eval(input(f'Digite o altura...: '))
        param_genero = eval(input(f'Digite o genero...: '))
        if param_genero == 1:
            print((78 * param_altura) - 58)
        else:
            print((59 * param_altura) - 44.8)


peso_altura_genero(2)
