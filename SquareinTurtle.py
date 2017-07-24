import turtle

sideLength = 200;

turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

turtle.goto(-100, -100 + sideLength)
turtle.goto(-100 + sideLength, -100 + sideLength)
turtle.goto(-100 + sideLength, -100 )
turtle.goto(-100, -100)


turtle.mainloop();
