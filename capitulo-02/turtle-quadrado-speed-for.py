import turtle


# Quadrado em várias velocidades
def desenha_quadrado(lado):
    """
    Desenha um quadrado de lado = lado
    """
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)


if __name__ == '__main__':
    # Devagarzinho
    turtle.speed(1)
    meu_lado = 50
    desenha_quadrado(meu_lado)

    turtle.exitonclick()
