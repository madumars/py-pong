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
ball.speed(60)
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
    "ball_speed": 5
}

time.sleep(10)

#Teclas
#sc.listen()
#sc.onkeypress(hurdleupA, "w")  
#sc.onkeypress(hurdledownA, "s") 
#sc.onkeypress(hurdlebupB, "Up")
#sc.onkeypress(hurdledownB, "Down")

#Mover a barreira (hurdle)




#Notas gerais 
#Fundo - bgcolor("white")
#goto é o salto, a instrução a partir de um ponto
#Fazer pontuação
#Cada trave ter uma cor diferente para depois associar a cada player
