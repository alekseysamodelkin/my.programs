# -----------------------------
# Program by Samodelkin
# -----------------------------

import turtle

def star():

  for step in range(6):
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(50)
        turtle.left(120)
    turtle.end_fill()

    turtle.forward(50)
    turtle.right(60)

def круг():
    turtle.circle(100,360,100)


turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('red', 'green')
turtle.speed(2)
turtle.screensize(5)


круг()
turtle.setposition(-25,140)
star()

turtle.hideturtle()
turtle.mainloop()

