import turtle

turtle.speed(0)
turtle.bgcolor("black")
for i in range (15):
    for colors in ("red", "green", "blue", "magenta", "yellow", "white"):
        turtle.color(colors)
        turtle.pensize(3)
        turtle.left(4)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)


