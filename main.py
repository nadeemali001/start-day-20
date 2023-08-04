import time
from turtle import Screen
from snake import Snake

scn = Screen()
snake = Snake()
#snake.__int__()

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

scn.exitonclick()
