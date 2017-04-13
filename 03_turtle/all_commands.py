import turtle

def onClick(x,y):
    turtle.fd(10)

def vierkant():
    for i in range(4):
        turtle.forward(20)
        turtle.right(90)
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()

turtle.speed(0)
turtle.shape("turtle")
turtle.bgcolor("orange")

turtle.home()
turtle.penup()
turtle.setx(-200)
turtle.pendown()
vierkant()

turtle.pensize(2)
vierkant()

turtle.write("tekst")

turtle.pensize(1)
turtle.pencolor((1, 0, 0))
vierkant()

turtle.write("tekst")

turtle.fillcolor("violet")
turtle.begin_fill()
vierkant()
turtle.end_fill()

turtle.circle(10)
turtle.circle(120, 180)

turtle.write("tekst")

turtle.onclick(onClick)

turtle.done()
