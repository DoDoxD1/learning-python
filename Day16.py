# from turtle import *
#
# my_turtle = Turtle()
# my_turtle.shape("turtle")
# my_turtle.color("coral")
# my_turtle.forward(100)
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import *

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
