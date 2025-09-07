import math


cubo = 3
constante = 4 / 3

param_raio = eval(input(f'Digite o valor do raio...: '))


def volume_esfera():
    print("Volume calculado: ", constante * math.pi * (param_raio ** cubo))


volume_esfera()
