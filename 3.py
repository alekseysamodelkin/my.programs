# -----------------------------
# Program by Samodelkin
# -----------------------------

import turtle

t = turtle
t.shape('turtle')
t.color("blue")
t.speed(20)
n = int(t.textinput(u"Количество лепестков.", "Введите количество окружностей: "))
x = 1
def цветок(x):
    while x <= n:
        t.circle(50)
        t.left(360 / n)
        x += 1
цветок(x)
t.mainloop()