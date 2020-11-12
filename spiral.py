import random
from turtle import Turtle, colormode

draw_circle = Turtle()
draw_circle.speed("fastest")
draw_circle.pensize(3)
colormode(255)


def draw_spiral(size, distanc=5):
    for i in range(0, 361, distanc):
        draw_circle.color(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256))
        draw_circle.circle(size)
        draw_circle.left(distanc)
