from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self,highest_score):
        super().__init__()
        self.highest_score = highest_score
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",font=15,align="center")

    def set_highest_score(self):
        if self.score>self.highest_score:
            self.highest_score = self.score

    def update_scoreboard(self):
        self.clear()
        self.write(f"your score: {self.score} High Score: {self.highest_score}",font=15,align="center")

    
    def increase_score(self):
        self.score+=1
    