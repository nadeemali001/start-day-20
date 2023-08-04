import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

scn = Screen()
snake = Snake()
food = Food()
score = Score()

scn.setup(width=600, height=600)
scn.bgcolor("black")
scn.title("My Snake Game")
scn.tracer(0)

scn.listen()
scn.onkey(snake.up, "Up")
scn.onkey(snake.down, 'Down')
scn.onkey(snake.left, 'Left')
scn.onkey(snake.right, 'Right')


game_on = True

while game_on:
    scn.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment_score()

scn.exitonclick()
