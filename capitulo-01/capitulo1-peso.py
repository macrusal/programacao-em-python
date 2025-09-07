altura_masculino = 1.81
altura_feminino = 1.81
peso_masculino = 72.7
peso_feminino = 62.1


# definindo funções
def peso(param_peso):
    return (param_peso * 1.81) - 58


def peso_altura(param_peso, param_altura):
    return (param_peso * param_altura) - 58


def peso_altura_genero(param_genero):
    param_altura = eval(input(f'Digite o altura...: '))
    param_peso = eval(input(f'Digite o peso...: '))
    if param_genero == 1:
        return (param_peso * param_altura) - 58
    else:
        return (param_peso * param_altura) - 58


for i in range(5):
    print("Cálculo de peso.......: ", peso_altura_genero(1))

# print("Masculino - PxA: ", (peso_masculino * altura_masculino) - 58)
# print("Peso...........: ", peso(peso_masculino))
# print("Peso e Altura..: ", peso_altura(peso_masculino, altura_masculino))
# print("Masculino......: ", peso_altura_genero(1))
