from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",font=15,align="center")

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score}",font=15,align="center")
        self.increase_score()
    
    def increase_score(self):
        self.score+=1

    def start_again(self):
        self.home()
    