# -----------------------------
# Program by Samodelkin
# -----------------------------

import turtle

t = turtle
t.shape('turtle')
t.color("blue")
t.speed(5)

n = int(turtle.textinput(u'Введите количество вершин', 'нечётное число: '))
def stars(n):
    t.left(180 - (180 / n))
    t.forward(200)
x = 1
while x <= n:
    stars(n)
    x += 1
t.hideturtle()
turtle.exitonclick()