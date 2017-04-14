from tkinter import *
from random import *

size = 500
window = Tk()
canvas = Canvas(window, width=size, height=size)


def teken_cirkel():
    d = int(text.get("1.0", END))
    aantal = int(text2.get("1.0", END))

    for i in range(aantal):
        col = choice(['dark red', 'red', 'black'])
        x0 = randint(0, size)
        y0 = randint(0, size)
        canvas.create_oval(x0, y0, x0 + d, y0 + d, fill=col)
    window.update()


text = Text(window, width=5, height=1)
text2 = Text(window, width=5, height=1)

text.insert(END, "10")
text2.insert(END, "100")
button1 = Button(window, text='teken cirkel', command=teken_cirkel)

canvas.grid(row=1, column=0, columnspan=5)

Label(window, text="aantal:").grid(row=0, column=0)
text2.grid(row=0, column=1)
Label(window, text="diameter:").grid(row=0, column=2)
text.grid(row=0, column=3)
button1.grid(row=0, column=4)

window.mainloop()
