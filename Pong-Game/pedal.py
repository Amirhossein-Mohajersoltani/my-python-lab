from turtle import Turtle
from time import sleep



SEGMENT_POSITION = [(0,0),(0,-20),(0,-40),(0,-60),(0,-80)]

class Pedal:
    def __init__(self,x,y):
        self.segments = []
        self.create_pedal()
        self.take_position(x,y)
        self.up_head = self.segments[0]
        self.up_head.left(90)
        self.down_head = self.segments[len(self.segments)-1]
        self.down_head.right(90)

    def create_pedal(self):
        for position in SEGMENT_POSITION:
            segment = Turtle(shape="square")
            segment.speed("fastest")
            segment.penup()
            segment.color("White")
            segment.goto(position)
            self.segments.append(segment)

    def take_position(self,x,y):
        self.segments[0].goto(x,y+20)
        self.segments[1].goto(x,y)
        self.segments[2].goto(x,y-20)
        self.segments[3].goto(x,y-40)
        self.segments[4].goto(x,y-60)
    
    def move_up(self):
        for segment_index in range(len(self.segments)-1,0,-1):
            next_segment = self.segments[segment_index-1]
            segment = self.segments[segment_index]
            segment.goto(next_segment.xcor(),next_segment.ycor())
        self.up_head.forward(20)

    def move_down(self):
        for segment_index in range(0,len(self.segments)-1):
            next_segment = self.segments[segment_index+1]
            segment = self.segments[segment_index]
            segment.goto(next_segment.xcor(),next_segment.ycor())
        self.down_head.forward(20)








