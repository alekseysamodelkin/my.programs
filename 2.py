# -----------------------------
# Program by Samodelkin
# -----------------------------

import turtle
turtle.speed(100)

def квадрат():
    for i in range(4):
        turtle.forward(90)
        turtle.right(90)

квадрат()


turtle.shape("turtle")
turtle.penup()
turtle.setposition(x=0, y=90)
turtle.pendown()
turtle.color('red')


def круг():
    turtle.circle(90,360,100)

круг()

turtle.penup()
turtle.setposition(x=-180, y=0)
turtle.pendown()
t=turtle



def more():
    x = 1
    y = 10
    while x <= 10:
        t.left(225)
        t.penup()
        t.forward((y**2/2)**0.5)
        t.left(135)
        t.pendown()
        t.forward(y*x)
        t.left(90)
        t.forward(y*x)
        t.left(90)
        t.forward(y*x)
        t.left(90)
        t.forward(y*x)
        t.left(90)
        x += 1



more()


turtle.penup()
turtle.setposition(x=0, y=90)
turtle.pendown()

def паук():
    x = 1
    while True:
        t.forward(88)
        t.stamp()
        t.backward(88)
        t.right(360 / 10)
        x += 1
        if (x%10) == 1:
            break
паук()

turtle.penup()
turtle.setposition(x=0, y=90)
turtle.pendown()

def квспираль():
    x = 1
    y = 20
    while x <= y:
        t.forward(5*x)
        t.left(90)
        x += 1

квспираль()

turtle.penup()
turtle.setposition(x=0, y=90)
turtle.pendown()

import math
def спираль():
    k = 0
    while True:
        t.forward(k / 2 * math.pi)
        turtle.left(2 * math.pi)
        k += 0.02

спираль()

turtle.mainloop()


