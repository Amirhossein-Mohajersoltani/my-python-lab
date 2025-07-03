from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x_coor = randint(-280,280)
        y_coor = randint(-280,280)
        self.setposition(x_coor,y_coor)

