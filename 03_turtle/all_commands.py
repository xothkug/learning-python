import turtle

def onClick(x,y):
    vierkant()

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
turtle.colormode(255)

turtle.home()
turtle.penup()
turtle.setx(-200)
turtle.pendown()
vierkant()

turtle.pensize(2)
vierkant()

turtle.write("tekst")

turtle.pensize(1)
turtle.pencolor((255, 0, 0))
vierkant()

turtle.write("tekst")

turtle.fillcolor("violet")
turtle.begin_fill()
vierkant()
turtle.end_fill()

turtle.circle(10)
turtle.circle(120, 90)

turtle.onclick(onClick)

turtle.done()
