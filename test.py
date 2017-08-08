import turtle
l = [(10000,      0),
     (0,  10000),
     (3000,   7000),
     (7000,   3000),
     (20000,  21000),
     (3000,   4000),
     (14000,  15000),
     (6000,   7000)]
turtle.width(2)
turtle.down
for e in l:
    turtle.up()
    x = e[0]/100
    y = e[1]/100
    turtle.goto(x, y)
    turtle.down()
    turtle.circle(1)
    turtle.write(str(e[0])+', '+str(e[1]))
turtle.mainloop()