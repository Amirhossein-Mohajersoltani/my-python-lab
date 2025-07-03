from snake import Snake
from turtle import Screen
from time import sleep
from food import Food
from scoreboard import ScoreBoard


try:
    with open("./day24-Files, Directories and Paths/second_problem/data.txt") as file:
        high_score = int(file.read())
except:
    high_score = 0

screen = Screen()

screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")

food = Food()

scoreboard = ScoreBoard(high_score)

screen.tracer(0)

snake = Snake()



screen.listen()

screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)


is_game_on = True

while is_game_on:
    screen.update()
    sleep(0.1)
    snake.move()
    # Detect collision with Food
    if snake.head.distance(food)<17:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        

    # Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        is_game_on = False

    # Detect collission with Tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.game_over()
            is_game_on = False


scoreboard.set_highest_score()

with open("./day24-Files, Directories and Paths/second_problem/data.txt",mode="w") as file:
    file.write(str(scoreboard.highest_score))


screen.exitonclick()





