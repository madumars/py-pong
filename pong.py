#ping pong em py

import turtle
import time

#Tela/Screen
turtle.setup(400, 300)
turtle.bgcolor("white")

'''
sc = turtle.Screen()
sc.title("Py pong")
sc.bgcolor("white")
sc.setup(400, 300)
'''

#Bola(ball)
ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
#ball.speed(30)
ball.dx = 5
ball.dy = -5
ball.penup()
ball.goto(0, 0)

game_over = False
winner = None
points = {
    "p1": 0,
    "p2": 0
}
game_rules = {
    "points_win": 3,
    "ball_speed": 3
}

#Barreiras 

#Barreira da Esquerda (hurdle_left)
hurdle_left = turtle.Turtle()
#hurdle_left.speed(0)
hurdle_left.shape("square")
hurdle_left.shapesize(stretch_wid=5, stretch_len=1)
hurdle_left.penup()
hurdle_left.goto(-350, 0)
hurdle_left.dy = 0
hurdle_left.color("purple")


#Barreira da Direita (hurdle_right)
hurdle_right = turtle.Turtle()
#hurdle_right.speed(0)
hurdle_right.shape("square")
hurdle_right.shapesize(stretch_wid=5, stretch_len=1)
hurdle_right.penup()
hurdle_right.dy = 0
hurdle_right.goto(350, 0)
hurdle_right.color("green")

#Game


#Painel pontuação (arrumar estilo depois)
score_display = turtle.Turtle()
score_display.color("blue")
score_display.penup() 
score_display.hideturtle()
score_display.goto(0, 200)
score_display.write("Jogador 1: 0 Jogador 2: 0", align="center", font=("Arial", 20, "normal"))

hurdle_left.sety(hurdle_left.ycor() + hurdle_left.dy)
hurdle_right.sety(hurdle_right.ycor() + hurdle_right.dy)
ball.setx(ball.xcor() + ball.dx)
ball.sety(ball.ycor() + ball.dy)

# Condições para o jogo
if points["p1"] == game_rules["points_win"]:
    game_over = True
    winner = "p1"
elif points["p2"] == game_rules["points_win"]:
    game_over = True
    winner = "p2"
    
    
if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < hurdle_right.ycor() + 50 and ball.ycor() > hurdle_right.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    
if(ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < hurdle_left.ycor() + 50 and ball.ycor() > hurdle_left.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        
#Não deixar a ball sair da tela

if ball.xcor() > 390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["p1"] += 1
elif ball.xcor() < -390:
    ball.goto(0, 0)
    ball.dx *= -1
    points["p2"] += 1
    
# Colidindo com o topo
if ball.ycor() > 290:
    ball.sety(290)
    ball.dy *= -1
elif ball.ycor() < -290:
    ball.sety(-290)
    ball.dy *= -1

#Testar de arrumar o placar
score_display.clear()
score_display.write("p1: {}  p2: {}".format(points["p1"], points["p2"]), align="center", font=("Arial", 24, "normal"))

#movimento da bola

def hurdle_left_up():
    hurdle_left.dy = 10
        
def hurdle_left_down():
    hurdle_left.dy = -10
        
def hurdle_right_up():
    hurdle_right.dy = 10
        
def hurdle_right_down():
    hurdle_right.dy = -10
        
#Teclas
turtle.listen()
turtle.onkeypress(hurdle_left_up, "w")  
turtle.onkeypress(hurdle_left_down, "s") 
turtle.onkeypress(hurdle_right_up, "Up")
turtle.onkeypress(hurdle_right_down, "Down")

#Tela de game over (precisa melhorar)
display_game_over = turtle.Turtle()
display_game_over.color("black")
display_game_over.penup()
display_game_over.hideturtle()
display_game_over.goto(0, 0)
display_game_over.write("Fim de jogo {} venceu".format(winner), align="center", font=("Arial", 24, "normal"))
    
#Game loop
while True:
    turtle.update()
    time.sleep(0.01)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
# não funcionou esse código 
#verificando bordas
    """
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
        score_display.clear()
        score_display.write("p1: {}  p2: {}".format(p1,p2), align="center", font=("Arial", 24, "normal"))
    
    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.dy *= -1
        p2 += 1
        score_display.clear()
        score_display.write("p1: {}  p2: {}".format(p1,p2), align="center", font=("Arial", 24, "normal"))
"""

#consertar:
# apertar o "s" coloca os itens no ponto de partida novamente e não desce e barra
# o jogo termina após marcar o primeiro ponto em qualquer lado acusando erro pro jogador que perdeu 
# arrumar tamanho da tela 
# pontuação não esta adicionando 

#Notas gerais 
#Fundo - bgcolor("white")
#goto é o salto, a instrução a partir de um ponto
#Fazer pontuação
#Cada trave ter uma cor diferente para depois associar a cada player
