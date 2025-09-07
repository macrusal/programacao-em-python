numero_adinha = 25
param_numero = eval(input(f'Digite o valor para da adivinha...: '))


def adivinha(numero):
    if numero == numero_adinha:
        return print(True)
    else:
        return print(False)


adivinha(param_numero)