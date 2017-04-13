import turtle

map_size = 10
the_map = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def leeg_vierkant(x, y):
    turtle.color('silver')
    turtle.pu()
    turtle.setposition(x * 10, - y * 10)
    turtle.pd()
    for i in range(4):
        turtle.fd(10)
        turtle.right(90)


def vierkant(x, y):
    turtle.color('black')
    turtle.pu()
    turtle.setposition(x * 10, - y * 10)
    turtle.pd()
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(10)
        turtle.right(90)
    turtle.end_fill()


def draw():
    turtle.clear()
    for yi, y in enumerate(the_map):
        for xi, x in enumerate(y):
            if x == 1:
                vierkant(xi, yi)
            else:
                leeg_vierkant(xi, yi)


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


def step():
    global the_map
    the_map = update_map()
    draw()


def screen_click(x, y):
    step()


screen = turtle.getscreen()
screen.delay(0)
screen.onclick(screen_click)

turtle.colormode(255)
turtle.speed(0)
turtle.hideturtle()

draw()

turtle.done()
