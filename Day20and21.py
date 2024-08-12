from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)
snake = []

for i in range(0, 3):
    box = Turtle("square")
    box.color("white")
    box.penup()
    box.setpos(0-(i*20), 0)
    snake.append(box)

screen.update()

game_on = True


def move_up():
    snake[0].right(90)


while game_on:
    screen.onkey(move_up, "w")
    for i in range(len(snake)-1, 0, -1):
        prev_box = snake[i-1]
        box = snake[i]
        box.goto(prev_box.xcor(), prev_box.ycor())
    snake[0].forward(20)
    screen.update()
    time.sleep(0.2)
    if snake[0].xcor() > 280:
        game_on = False

screen.exitonclick()

# https://github.com/DoDoxD1/snake-game-python
