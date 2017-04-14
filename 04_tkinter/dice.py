from tkinter import *
from random import randint


def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(1, 6)))


window = Tk()
text = Text(window, width=3, height=1)
button1 = Button(window, text='press to roll the dice', command=roll)

text.pack()
button1.pack()

window.mainloop()
