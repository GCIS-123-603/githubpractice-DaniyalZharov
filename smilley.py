import turtle as t
def face():
    t.penup()
    t.goto(0,0)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def nose():
    t.penup()
    t.right(270)
    t.forward(70)
    t.right(90)
    t.pendown()
    t.fillcolor("pink")
    t.begin_fill()
    t.circle(20)
    t.end_fill

def eye1(a, b, c):
    t.up()
    t.goto(40,40)
    t.forward(a)
    t.left(90)
    t.down()
    t.pencolor("black")
    t.pensize(2)
    t.fillcolor("white")
    t.begin_fill()
    t.circle(a)
    t.end_fill()
    t.up()
    t.goto(40,40)
    t.forward(b)
    t.left(90)
    t.down()
    t.pencolor("black")
    t.pensize(2)
    t.fillcolor("white")

face()
nose()
eye1()

