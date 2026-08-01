import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Heart")

t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.hideturtle()

colors = [
    "red",
    "blue",
    "cyan",
    "yellow",
    "magenta",
    "orange",
    "lime",
    "pink",
    "purple",
    "white"
]

for i in range(120):
    t.penup()
    t.goto(0, 40)

    angle = i * (math.pi * 2) / 120

    x = 16 * (math.sin(angle) ** 3)

    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )

    x *= 15
    y *= 15

    t.color(random.choice(colors))
    t.pendown()
    t.goto(x, y)

    for _ in range(8):
        t.forward(6)
        t.backward(6)
        t.right(45)

turtle.done()
