




from turtle import Turtle,Screen
from pedal import Pedal
from time import sleep
from ball import Ball
from scoreboard import ScoreBoard

# dash_line
dash_line = Turtle()
dash_line.hideturtle()
dash_line.speed("fastest")
dash_line.penup()
dash_line.goto(0,400)
dash_line.pendown()
dash_line.color('white')
dash_line.right(90)
for i in range(40):
    dash_line.forward(10)
    dash_line.penup()
    dash_line.forward(10)
    dash_line.pendown()

# this leverage helps to control pedals while they are swinging
go_up_pedal1 = True
go_up_pedal2 = True

pedal_1_board = ScoreBoard(-50,350)
pedal_2_board = ScoreBoard(50,350)

def go_up_pedal_1():
    global go_up_pedal1
    go_up_pedal1 = True

def go_down_pedal_1():
    global go_up_pedal1
    go_up_pedal1 = False

def go_up_pedal_2():
    global go_up_pedal2
    go_up_pedal2 = True

def go_down_pedal_2():
    global go_up_pedal2
    go_up_pedal2 = False

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1920,height=1080,startx=0,starty=0)
screen.tracer(0)
screen.listen()


pedal_1 = Pedal(-750,0)
pedal_2 = Pedal(743,0)

ball = Ball()

screen.onkey(key='w',fun=go_up_pedal_1)
screen.onkey(key='s',fun=go_down_pedal_1)

screen.onkey(key='Up',fun=go_up_pedal_2)
screen.onkey(key='Down',fun=go_down_pedal_2)

is_game_on = True
while is_game_on:

    screen.update()
    sleep(0.06)
    ball.move()


    if pedal_1.up_head.ycor()>= 400:
        go_up_pedal1 = False
    elif pedal_1.down_head.ycor()<= -400:
        go_up_pedal1 = True

    if pedal_2.up_head.ycor()>= 400:
        go_up_pedal2 = False
    elif pedal_2.down_head.ycor()<= -400:
        go_up_pedal2 = True

    if go_up_pedal1:
        pedal_1.move_up()
    else:
        pedal_1.move_down()

    if go_up_pedal2:
        pedal_2.move_up()
    else:
        pedal_2.move_down()

    # Ball


    if ball.ycor() >= 370 or ball.ycor() <= -370:
        new_angle = ball.wall_angle()
        ball.setheading(new_angle)

    for segment in pedal_1.segments:
        if ball.distance(segment)<20:
            new_angle = ball.pedal_angle()
            ball.setheading(new_angle)
            ball.move()

    for segment in pedal_2.segments:
        if ball.distance(segment)<20:
            new_angle = ball.pedal_angle()
            ball.setheading(new_angle)
            ball.move()

    if ball.xcor()<-770:
        pedal_2_board.update_scoreboard()
        ball.start_again()
    elif ball.xcor()>770:
        pedal_1_board.update_scoreboard()
        ball.start_again()













screen.exitonclick()