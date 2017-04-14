from tkinter import *
import random

autorun = False
step_nr = 1
# create map
map_size = 40
cell_size = 10
the_map = []


def empty_map():
    global the_map
    the_map = []
    for y in range(map_size):
        row = []
        for x in range(map_size):
            row.append(0)
        the_map.append(row)


def random_map():
    global the_map
    the_map = []
    for y in range(map_size):
        row = []
        for x in range(map_size):
            row.append(1 if random.randint(0, 100) > 75 else 0)
        the_map.append(row)


random_map()


def get_neighbours(xi, yi):
    count = 0
    neighbors = []

    if yi > 0 and xi > 0 and the_map[yi - 1][xi - 1] == 1:
        neighbors.append('tl')
        count += 1
    if xi > 0 and the_map[yi][xi - 1] == 1:
        neighbors.append('t')
        count += 1
    if yi < map_size - 1 and xi > 0 and the_map[yi + 1][xi - 1] == 1:
        neighbors.append('tr')
        count += 1

    if yi > 0 and the_map[yi - 1][xi] == 1:
        neighbors.append('l')
        count += 1
    if yi < map_size - 1 and the_map[yi + 1][xi] == 1:
        neighbors.append('r')
        count += 1

    if yi > 0 and xi < map_size - 1 and the_map[yi - 1][xi + 1] == 1:
        neighbors.append('bl')
        count += 1
    if xi < map_size - 1 and the_map[yi][xi + 1] == 1:
        neighbors.append('b')
        count += 1
    if yi < map_size - 1 and xi < map_size - 1 and (the_map[yi + 1][xi + 1] == 1):
        neighbors.append('br')
        count += 1

    return neighbors


def update_map():
    new_map = []
    for yi, y in enumerate(the_map):
        new_y = []
        for xi, x in enumerate(y):
            neighbours = get_neighbours(xi, yi)
            count = len(neighbours)
            if x == 1:
                if count == 2 or count == 3:
                    new_y.append(1)
                else:
                    new_y.append(0)
            else:
                if count == 3:
                    new_y.append(1)
                else:
                    new_y.append(0)
        new_map.append(new_y)
    return new_map


def draw():
    canvas.delete("all")
    for yi, y in enumerate(the_map):
        for xi, x in enumerate(y):
            if x == 1:
                canvas.create_rectangle(xi * cell_size, yi * cell_size, xi * cell_size + cell_size,
                                        yi * cell_size + cell_size, fill="black")


def step():
    global the_map, step_nr
    step_nr += 1
    the_map = update_map()
    draw()


def step_action():
    step()


def start_action():
    global autorun
    autorun = True;


def clear_action():
    global step_nr
    stop_action()
    step_nr = 1
    empty_map()
    draw()


def stop_action():
    global autorun
    autorun = False;


def change_cell_action(event):
    xi = event.x // cell_size
    yi = event.y // cell_size
    if xi < map_size and yi < map_size:
        the_map[yi][xi] = -1 * (the_map[yi][xi] - 1)
        draw()


size = 500
window = Tk()
canvas = Canvas(window, width=map_size * cell_size, height=map_size * cell_size, bg='white')
button_step = Button(window, text='step', command=step_action)
button_start = Button(window, text='start', command=start_action)
button_stop = Button(window, text='stop', command=stop_action)
button_clear = Button(window, text='clear', command=clear_action)

Label(window, text="step nr:").grid(row=0, column=0)

var = StringVar('')
label = Label(window, textvariable=var)
label.grid(row=0, column=1)

button_step.grid(row=0, column=2)
button_start.grid(row=0, column=3)
button_stop.grid(row=0, column=4)
button_clear.grid(row=0, column=5)
canvas.grid(row=1, column=0, columnspan=6)

canvas.bind('<Button-1>', change_cell_action)

draw()
while True:
    if autorun:
        step()

    var.set(str(step_nr))

    window.update_idletasks()
    window.update()
