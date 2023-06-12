import turtle
import random

turtle.title('Tentativa de jogo')
turtle.setup(550,550)
turtle.bgcolor("black")

#Comida
comida=turtle.Pen()
comida.hideturtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.shapesize(0.2,0.2,0.2)
comida.setposition(random.randint(-225,225),random.randint(-225,225))

#Definiçoes
drawing=turtle.Pen()
snake=turtle.Pen()
snake.shape('turtle')
snake.penup()
score=turtle.Pen()
dificuldade=turtle.Pen()
easy=turtle.Pen()
medium=turtle.Pen()
hard=turtle.Pen()
dificuldade.speed(10)
easy.speed(10)
medium.speed(10)
hard.speed(10)

#Reset do jogo
def reset1():
    comida.shapesize(0.2,0.2,0.2)
    snake.shapesize(1,1,1)
    score.clear()
    comida.hideturtle()
    snake.speed(0)
    drawing.clear()
    turtle.bgcolor('black')
    snake.hideturtle()
    snake.setpos(0,0)
    hide_all()
    comida.setpos(random.randint(-225,225),random.randint(-225,225))
    interface()

    
def hide_all():
    snake.hideturtle()
    comida.hideturtle()
    dificuldade.hideturtle()
    easy.hideturtle()
    medium.hideturtle()
    hard.hideturtle()
    score.hideturtle()

#Interface inicial
def interface():
    r=0
    score.clear()
    hide_all()
    easy.color('white')
    medium.color('white')
    hard.color('white')
    dificuldade.color('white')
    dificuldade.penup()
    dificuldade.setpos(-100,100)
    dificuldade.write('Dificuldade:' , font=(None,35,'bold'))
    easy.penup()
    medium.penup()
    hard.penup()
    easy.setpos(-68,75)
    easy.write('1. Easy (Press 1)', font=(None,15,'bold'))
    medium.setpos(-68,50)
    medium.write('2. Medium (Press 2)', font=(None,15,'bold'))
    hard.setpos(-68,25)
    hard.write('3. Hard (Press 3)', font=(None,15,'bold'))


def easy1():
    if snake.pos()==(0,0):
        turtle.bgcolor('green')
        snake.setpos(0,0)
        dificuldade.clear()
        easy.clear()
        medium.clear()
        hard.clear()
        snake.showturtle()
        comida.showturtle()
        snake.speed(1)
        inf_loop()

def medium1():
    if snake.pos()==(0,0):
        turtle.bgcolor('green')
        snake.setpos(0,0)
        dificuldade.clear()
        easy.clear()
        medium.clear()
        hard.clear()
        snake.showturtle()
        comida.showturtle()
        snake.speed(1.5)
        inf_loop()

def hard1():
    if snake.pos()==(0,0):
        turtle.bgcolor('green')
        snake.setpos(0,0)
        dificuldade.clear()
        easy.clear()
        medium.clear()
        hard.clear()
        snake.showturtle()
        comida.showturtle()
        snake.speed(3)
        inf_loop()


#Score
score.hideturtle()
score.penup()
score.setpos(-230,230)
score.speed(0)
score.color('White')

#Limites do jogo
def limite():
    xcor=snake.xcor()
    ycor=snake.ycor()
    if abs(xcor)>225:
        snake.hideturtle()
        snake.setposition(-xcor,ycor)
        if -xcor<0:
            snake.seth(0)
        if -xcor>0:
            snake.seth(180)
        snake.forward(10)
        snake.showturtle()
    if abs(ycor)>225:
        snake.hideturtle()
        snake.setposition(xcor,-ycor)
        if -ycor<0:
            snake.seth(90)
        if -ycor>0:
            snake.seth(270)
        snake.forward(10)
        snake.showturtle()


#Comida funcao
def comida_function():
    comida.hideturtle()
    comida.shapesize(comida.shapesize()[0]+0.05,comida.shapesize()[1]+0.05,comida.shapesize()[2]+0.05)
    comida.setposition(random.randint(-225,225),random.randint(-225,225))
    comida.showturtle()
    
#Andar
def up():
    if not (snake.heading()==90 or snake.heading()==180+90):
        snake.penup()
        snake.seth(90)

def left():
    if not (snake.heading()==0 or snake.heading()==180):
        snake.penup()
        snake.seth(180)

def right():
    if not (snake.heading()==0 or snake.heading()==180):
        snake.penup()
        snake.seth(0)

def down():
    if not (snake.heading()==90 or snake.heading()==-90):
        snake.penup()
        snake.seth(-90)

'''============================================'''


#Clique nas teclas
turtle.onkey(down,'Down')
turtle.onkey(up,"Up")
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')
turtle.onkey(reset1,'r')
turtle.onkey(reset1,'R')
turtle.onkey(easy1,'1')
turtle.onkey(medium1,'2')
turtle.onkey(hard1,'3')
turtle.listen()


#por comida visivel
def inf_loop():
    #Barreiras
    drawing.color('white') #Cor da barreira
    drawing.speed(10)
    drawing.hideturtle()
    drawing.penup()
    drawing.setposition(225,225)
    drawing.pendown()
    drawing.setposition(-225,225)
    drawing.setposition(-225,-225)
    drawing.setposition(225,-225)
    drawing.setposition(225,225)
    '''====================='''
    sc=0
    a=10 #distancia a que pode comer a bola
    score.write('Your score is: %s' %sc, font=(None, 11, "bold"))
    
    #Movement
    while True:
        xcor=snake.xcor()
        ycor=snake.ycor()
        x0=comida.xcor()
        y0=comida.ycor()
        limite()
        snake.forward(snake.speed())
        if x0-a<xcor<x0+a and y0-a<ycor<y0+a:
            comida_function()
            snake.shapesize(snake.shapesize()[0]+0.2,snake.shapesize()[1]+0.2,snake.shapesize()[2]+0.2)
            a=a+0.05*(a)
            sc=sc+10
            score.clear()
            score.write('Your score is: %s' %sc, font=(None, 11, "bold"))



interface()  #comecar com interface aka jogo
turtle.done()
