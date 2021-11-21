from turtle import *
import MainGUI

def day1draw():
    setup(500, 500)
    title("Test")
    hideturtle()
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    bgcolor("black")
    speed(0)
    for x in range(10):
        pencolor(colors[x%6])
        width(x//100 + 1)
        forward(x)
        left(59)
    exitonclick()
