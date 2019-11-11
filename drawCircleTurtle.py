from turtle import Turtle

def drawCircle(t, x, y, r):
    t.up()
    t.goto(x, y)
    t.forward(200)
    t.down()
    t.left(90)
    distance = 2.0 * 3.14 * r /120.0
    for x in range(120):
        t.left(3)
        t.forward(distance)
    
def main():
    t = Turtle()
    drawCircle(t, 10, 10, 50)
    drawCircle(t, 30, 40, 100)
    drawCircle(t, 50, 30, 200)

main()
