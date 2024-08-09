import turtle as timmy
import random


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)


screen = timmy.Screen()
screen.colormode(255)
screen.setup(500, 400)
# draw shapes
# for i in range(10):
#     sides = i + 3
#     angle = 360/sides
#     change_color()
#     for j in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)

# draw random walk
# timmy.pensize(10)
# for i in range(200):
#     change_color()
#     timmy.forward(random.choice(range(50)))
#     timmy.right(random.choice([90, 180, 270]))

# draw spirograph
timmy.speed("fastest")
# for i in range(36):
#     timmy.circle(100)
#     timmy.setheading(timmy.heading()+10)
#     change_color()

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71),
              (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229),
              (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9),
              (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

# palate = colorgram.extract("img.jpg", 30)
# for color in palate:
#     color_list.append((color.rgb.r, color.rgb.g, color.rgb.b))
# print(color_list)

# timmy.right(90)
# timmy.penup()
# timmy.forward(300)
# timmy.right(90)
# timmy.forward(380)
# timmy.left(180)
timmy.penup()
# timmy.goto(-200, -185)

for i in range(10):
    timmy.goto(-225, -175 + (i * 50))
    for j in range(10):
        # timmy.color(random.choice(color_list))
        timmy.dot(20, random.choice(color_list))
        timmy.penup()
        timmy.forward(50)


screen.exitonclick()
