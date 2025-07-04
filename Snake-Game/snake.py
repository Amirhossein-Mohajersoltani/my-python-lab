from turtle import Turtle

POSITION_SEGMENT = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):     
        for position in POSITION_SEGMENT:
            self.add_segment(position)

    def add_segment(self , position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_index in range(len(self.segments)-1,0,-1):
            x = self.segments[seg_index-1].xcor()
            y = self.segments[seg_index-1].ycor()
            self.segments[seg_index].setpos(x,y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

