import turtle


# Quadrado em várias velocidades
def desenha_quadrado(lado):
    """
    Desenha um quadrado inclinado e defeituoso de lado = lado
    """
    turtle.goto(90, 90)
    turtle.setheading(45)
    for i in range(4):
        turtle.forward(lado)
        turtle.right(90)
    turtle.hideturtle()


if __name__ == '__main__':
    # Devagarzinho
    turtle.speed(1)
    meu_lado = 90
    desenha_quadrado(meu_lado)

    turtle.exitonclick()
