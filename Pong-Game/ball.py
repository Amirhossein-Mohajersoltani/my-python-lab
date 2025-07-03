from turtle import Turtle
from random import randint,choice

ball_direction = [randint(-45,45),randint(135,225)]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.setheading(choice(ball_direction))
    
    def move(self):
        self.forward(20)

    def pedal_angle(self):
        current_angle = self.heading()
        next_angle = 90-(current_angle-90)+randint(-15,15)
        return next_angle
    
    def wall_angle(self):
        current_angle = self.heading()
        next_angle = -current_angle
        return next_angle
    
    def start_again(self):
        self.home()
        self.setheading(choice(ball_direction))

