import turtle

turtle.speed(0)
screen = turtle.getscreen()
screen.delay(0)
straal_cirkel = 0

while True:
    turtle.circle(straal_cirkel, 180)
    straal_cirkel += 2
