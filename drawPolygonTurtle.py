def drawPolygon(t, vertices):
    t.up()
    (x ,y) = vertices[-1]
    t.goto(x ,y)
    t.down()
    for(x ,y) in vertices:
        t.goto(x ,y)
