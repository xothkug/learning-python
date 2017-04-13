import turtle
import lib.myturtle

screen = turtle.getscreen()
screen.delay(0)

turtle.colormode(255)
turtle.speed(0)
turtle.hideturtle()

turtle.pensize(0)

for y in range(20):
    turtle.penup()
    turtle.setposition(0, y * 10)
    turtle.pendown()
    for x in range(20):
        turtle.penup()
        turtle.setposition(x * 10, y * 10)
        turtle.pendown()
        color = lib.myturtle.get_random_color()
        turtle.color(color)
        turtle.begin_fill()
        lib.myturtle.square()
        turtle.end_fill()

turtle.done()
