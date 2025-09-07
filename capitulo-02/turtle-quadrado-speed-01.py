import turtle

# Quadrado em várias velocidades
def desenha_quadrado():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

# Devagarzinho
turtle.speed(1)
desenha_quadrado()

# Pausa para você ver o primeiro
turtle.clear()

# Médio (mais rápido)
turtle.speed(5)
desenha_quadrado()

# Pausa e limpa
turtle.clear()

# Instantâneo (só aparece pronto)
turtle.speed(0)
desenha_quadrado()

turtle.exitonclick()
