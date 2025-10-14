#ping pong em py

import turtle
import time

#Tela/Screen(sc)
sc = turtle.Screen()
sc.title("Py pong")
sc.bgcolor("white")
sc.setup(width=900, height=500)

#Bola(ball)
ball = turtle.Turtle()
ball.shape("circle")
ball.color("black")
ball.speed(30)
ball.dx = 5
ball.dy = -5
ball.penup()
ball.goto(0, 0)

#Barreiras 

#Barreira da Esquerda (hurdle_left)
hurdle_left = turtle.Turtle()
hurdle_left.speed(0)
hurdle_left.shape("square")
hurdle_left.shapesize(stretch_wid=6, stretch_len=2)
hurdle_left.penup()
hurdle_left.goto(-400, 0)
hurdle_left.color("purple")


#Barreira da Direita (hurdle_right)
hurdle_right = turtle.Turtle()
hurdle_right.speed(0)
hurdle_right.shape("square")
hurdle_right.shapesize(stretch_wid=6, stretch_len=2)
hurdle_right.penup()
hurdle_right.goto(400, 0)
hurdle_right.color("green")

#Game
game_over = False
Winner = None
points = {
    "p1": 0,
    "p2": 0
}
game_rules = {
    "win_points": 4,
    "ball_speed": 2
}

#Painel pontuação (arrumar estilo depois)
score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 200)
score_display.write("Jogador 1: 0 Jogador 2: 0", align="center", font=("Arial", 20, "normal"))

#movimento da bola

def hurdle_left_up():
    y = hurdle_left.ycor()
    if y < 250:
        y += 20
        hurdle_left.sety(y)
        
def hurdle_left_down():
    y = hurdle_left.ycor()
    if y > -240:
        y -= 20
        hurdle_right.sety(y)
        
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
        
#Teclas
sc.listen()
sc.onkeypress(hurdle_left_up, "w")  
sc.onkeypress(hurdle_left_down, "s") 
sc.onkeypress(hurdle_right_up, "Up")
sc.onkeypress(hurdle_right_down, "Down")
    
#Game loop
while True:
    sc.update()
    time.sleep(0.01)

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #if points["p1"] == game_rules["win_points"]:
       # game_over = True
       # winner = p1
    #elif points["p2"] == game_rules["win_points"]:
       # game_over= True
        #ss
        #winner = p2

#verificando bordas
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

    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < hurdle_right.ycor() + 50 and ball.ycor() > hurdle_right.ycor() - 50):
        ball.setx(360)
        ball.dx *= -1
    
    if(ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < hurdle_left.ycor() + 50 and ball.ycor() > hurdle_left.ycor() - 50):
        ball.setx(-360)
        ball.dx *= -1
    

#consertar:
# apertar o "s" coloca os itens no ponto de partida novamente e não desce e barra
# o jogo termina após marcar o primeiro ponto em qualquer lado acusando erro pro jogador que perdeu 

#Notas gerais 
#Fundo - bgcolor("white")
#goto é o salto, a instrução a partir de um ponto
#Fazer pontuação
#Cada trave ter uma cor diferente para depois associar a cada player
