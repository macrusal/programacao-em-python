numero_adinha = 25
param_range = eval(input(f'Digite o numero de tentativas.....: '))


def adivinha():
    for i in range(param_range):
        param_numero = eval(input(f'Digite o numero secreto...: '))
        if param_numero == numero_adinha:
            print(True)
        else:
            print(False)


adivinha()