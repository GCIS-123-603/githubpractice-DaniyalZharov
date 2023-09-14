import turtle
angle1 = 80
angle2 = 40
angle3 = 20
def square(x, y, z, angle1, angle2, angle3):
    turtle.pencolor("blue")
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.left(angle1)
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)
    turtle.end_fill()
    turtle.pencolor("blue")
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.left(angle2)
    for i in range(4):
        turtle.forward(y)
        turtle.left(90)
    turtle.end_fill()
    turtle.pencolor("blue")
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.left(angle3)
    for i in range(4):
        turtle.forward(z)
        turtle.left(90)
    turtle.end_fill()
turtle.bgcolor("black")

square(250, 200, 150, angle1, angle2, angle3)


    