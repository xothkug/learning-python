from random import *
from tkinter import *

size = 500
window = Tk()
canvas = Canvas(window, width=size, height=size)
canvas.pack()
while True:
    col = choice(['dark red', 'red', 'black'])
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/10)
    canvas.create_oval(x0,y0,x0+d,y0+d, fill=col)
    window.update()