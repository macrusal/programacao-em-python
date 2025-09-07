import turtle


def desenha_pentagono(lado):
    """
    Desenha um pentagono de lado = lado = lado
    """
    for i in range(5):
        turtle.forward(lado)
        turtle.right(72)
    turtle.hideturtle()


if __name__ == '__main__':
    # Devagarzinho
    turtle.speed(1)
    meu_lado = 130
    desenha_pentagono(meu_lado)

    turtle.exitonclick()
