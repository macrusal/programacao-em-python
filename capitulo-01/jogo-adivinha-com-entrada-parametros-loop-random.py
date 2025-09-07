import random

constante_limite_inferior = 1
constante_limite_superior = 100
numero_adivinha = random.randrange(1, 100)
param_range = eval(input(f'Digite o numero de tentativas.....: '))


def adivinha():
    for i in range(param_range):
        param_numero = eval(input(f'Digite um numero entre {constante_limite_inferior} e {constante_limite_superior}...: '))
        if param_numero < constante_limite_inferior or param_numero > constante_limite_superior:
            print(f'O numero digitado {param_numero} é invalido!')
        else:
            if param_numero == numero_adivinha:
                print('Voce acertou!')
            else:
                print(f'Voce errou, {param_numero} não é o numero secreto!')
        if i == param_range - 1:
            print(f'### Melhor sorte da proxima vez! ###')


adivinha()