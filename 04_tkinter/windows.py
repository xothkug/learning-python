from tkinter import *
import time

window = Tk()


def button_on_click():
    print('ok')


button = Button(window, text='dd', command=button_on_click)
button.pack()

canvas = Canvas(window, width=500, height=350)
canvas.pack()

rect = canvas.create_rectangle(50, 50, 100, 100)
window.update()

while True:
    canvas.move(rect, 1, 0)
    window.update()
    time.sleep(0.01)

window.mainloop()
