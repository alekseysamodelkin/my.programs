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

turtle.shape('turtle')
turtle.shapesize(1)
turtle.color('red', 'green')
turtle.speed(5)

star()

turtle.hideturtle()
turtle.mainloop()

