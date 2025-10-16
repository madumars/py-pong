import turtle
import time

# Tela/Screen(sc)
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# hurdle left(obstaculo)
hurdle_left = turtle.Turtle()
hurdle_left.speed(0)
hurdle_left.shape("square")
hurdle_left.color("purple")
hurdle_left.shapesize(stretch_wid=6, stretch_len=2)
hurdle_left.penup()
hurdle_left.goto(-400, 0)

# Right hurdle(obstaculo)
hurdle_right = turtle.Turtle()
hurdle_right.speed(0)
hurdle_right.shape("square")
hurdle_right.color("green")
hurdle_right.shapesize(stretch_wid=6, stretch_len=2)
hurdle_right.penup()
hurdle_right.goto(400, 0)

# bola (ball)
ball = turtle.Turtle()
ball.speed(4)  
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

# pontuação
p1 = 0
p2 = 0

# pontuação inicial
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("black")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("p1 : 0    p2: 0",
             align="center", font=("Courier", 24, "normal"))

# como mover o hurdle


def hurdle_left_up():
    y = hurdle_left.ycor()
    if y < 250:  
        y += 20
        hurdle_left.sety(y)


def hurdle_left_down():
    y = hurdle_left.ycor()
    if y > -240:  
        y -= 20
        hurdle_left.sety(y)


def hurdle_right_up():
    y = hurdle_right.ycor()
    if y < 250:  
        y += 20
        hurdle_right.sety(y)


def hurdle_right_down():
    y = hurdle_right.ycor()
    if y > -240:  
        y -= 20
        hurdle_right.sety(y)


# teclas
sc.listen()
sc.onkeypress(hurdle_left_up, "w")  
sc.onkeypress(hurdle_left_down, "s")  
sc.onkeypress(hurdle_right_up, "Up")
sc.onkeypress(hurdle_right_down, "Down")

#game over
game_over = False
Winner = None
game_rules = {
    "win_points" : 5
}

#tela de game over
game_over_display = turtle.Turtle()
game_over_display.color("black")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)
game_over_display.write("Fim de jogo {} venceu!!!".format(Winner), align="center", font=("Arial", 24, "normal"))

# game looping
while True:
    sc.update()
    time.sleep(0.01) 
     
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    
    # confirmar bordas
    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.goto(0, 0)
        ball.dy *= -1
        p1 += 1
        sketch.clear()
        sketch.write("p1 : {}    p2: {}".format(
            p1, p2), align="center",
            font=("Courier", 24, "normal"))

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        p2 += 1
        sketch.clear()
        sketch.write("p1 : {}    p2: {}".format(
            p1, p2), align="center",
            font=("Courier", 24, "normal"))

    # colisão no hurdle
    if (ball.xcor() > 360 and ball.xcor() < 370) and \
            (ball.ycor() < hurdle_right.ycor() + 50 and ball.ycor() > hurdle_right.ycor() - 50):
        ball.setx(360)
        ball.dx *= -1

    if (ball.xcor() < -360 and ball.xcor() > -370) and \
            (ball.ycor() < hurdle_left.ycor() + 50 and ball.ycor() > hurdle_left.ycor() - 50):
        ball.setx(-360)
        ball.dx *= -1
        
#consertar:
# arrumar tamanho da tela 
# arrumar tela de game over
# arrumar win e dar um ganhador


#arrumados
# pontuação não esta adicionando (ok)
# o jogo termina após marcar o primeiro ponto em qualquer lado acusando erro pro jogador que perdeu (ok)
# apertar o "s" coloca os itens no ponto de partida novamente e não desce e barra (ok)

#Notas gerais 
#Fundo - bgcolor("white")
#goto é o salto, a instrução a partir de um ponto
#Fazer pontuação
#Cada trave ter uma cor diferente para depois associar a cada player