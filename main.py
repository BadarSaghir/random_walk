# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from turtle import Turtle, Screen

colors = ["medium blue", "steel blue", "gold", "dark magenta", "dark red", "dark green",
          "dark slate blue", "sandy brown", "slate gray", "chartreuse", "dodger blue", "saddle brown"
          ]


def viewInScreen():
    screen = Screen()
    screen.exitonclick()

def forward():
    global solma
    for i in range(1, random.randrange(1, 6)):
        solma.forward(5)

def direction():
    global  solma
    solma.color(colors[random.randrange(0, len(colors))])
    prob_l = random.randrange(0, 3)/2
    prob_r = 1-prob_l
    if prob_r > prob_l:
        solma.right(random.randrange(0, 361))
    elif prob_r < prob_l:
        solma.left(random.randrange(0, 361))
    else:
        solma.forward(random.randrange(0, 10))


solma = Turtle()
solma.pensize(11)
# solma.forward(100)
for i in range(0, 1000):
    direction()
    forward()

viewInScreen()
