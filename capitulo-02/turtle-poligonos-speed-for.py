import turtle


def desenha_poligono(lado, numero_lados):
    """
    Desenha um pentagono regular qualquer
    """
    angulo_viragem = 360 / numero_lados
    for i in range(numero_lados):
        turtle.forward(lado)
        turtle.right(angulo_viragem)
    turtle.hideturtle()


if __name__ == '__main__':
    # Devagarzinho
    turtle.speed(1)
    meu_lado = 1
    numero_lados = 360
    desenha_poligono(meu_lado, numero_lados)

    turtle.exitonclick()
