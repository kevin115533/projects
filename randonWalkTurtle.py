from turtle import Turtle
import random

def randomWalk(t ,turns, distance = 20):
    for x in range(turns):
        t.left(random.randint(0 ,360))
        t.forward(distance)
