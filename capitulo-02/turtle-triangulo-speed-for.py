import turtle


def desenha_triangulo(lado):
    """
    Desenha um triangulo de lado = lado = lado
    """
    for i in range(3):
        turtle.forward(lado)
        turtle.right(120)
    turtle.hideturtle()


if __name__ == '__main__':
    # Devagarzinho
    turtle.speed(1)
    meu_lado = 130
    desenha_triangulo(meu_lado)

    turtle.exitonclick()
