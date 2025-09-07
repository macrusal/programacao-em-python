# definindo funções
def peso_altura_genero(param_genero):
    param_altura = eval(input(f'Digite o altura...: '))
    param_peso = eval(input(f'Digite o peso...: '))
    if param_genero == 1:
        return (param_peso * param_altura) - 58
    else:
        return (param_peso * param_altura) - 58


for i in range(5):
    print("Cálculo de peso.......: ", peso_altura_genero(1))
