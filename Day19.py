import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

user_color = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(0, 6):
    tim = Turtle("turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-240, y=(-100+(i*40)))
    turtles.append(tim)

race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_color:
                print(f"You won! {turtle.pencolor()}")
            else:
                print(f"You lost! {turtle.pencolor()} won")
            race_is_on = False
        turtle.forward(random.randint(0, 10))

# def forward():
#     turtle.forward(10)
#
#
# def backward():
#     turtle.backward(10)
#
#
# def right():
#     turtle.setheading(turtle.heading()+10)
#
#
# def left():
#     turtle.setheading(turtle.heading()-10)
#
#
# def clear():
#     turtle.clear()
#     turtle.penup()
#     turtle.home()
#     turtle.pendown()


# screen.listen()
# screen.onkey(forward, "w")
# screen.onkey(backward, "s")
# screen.onkey(right, "a")
# screen.onkey(left, "d")
# screen.onkey(clear, "c")
screen.exitonclick()
