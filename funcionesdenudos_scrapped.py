import turtle
import random as r

t = turtle.Turtle()
v = turtle.Screen()
v.tracer(0)


def palo():
    t.penup()
    grosor = 45
    angulo = 135
    largo = 100
    inicial = t.pos()
    t.width(grosor)
    t.setheading(angulo)
    t.pendown()
    t.forward(largo)
    final = t.pos()

    return grosor, angulo, largo, inicial, final


t.setheading(0)
t.penup()
t.pendown()
t.width(1)


def nudos(g, a, l, i, f):
    nodos = []
    t.pencolor("magenta")
    t.penup()
    t.goto(*i)
    t.setheading(90)
    t.goto(i[0] - r.uniform(-g / 2, g / 2), i[1])
    t.setheading(a)
    t.forward(r.uniform(-g / 2, l + g / 2))
    nodos.append(t.pos())

    for nodo in nodos:

        t.penup()
        t.goto(nodo)
        t.pendown()
        t.dot(1)

    # t.width(g)
    # t.setheading(a)
    # t.forward(l)


for _ in range(10):
    gro, ang, lar, ini, fin = palo()
    nudos(gro, ang, lar, ini, fin)
    t.setheading(0)
v.update()
turtle.done()
