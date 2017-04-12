import turtle

turtle.speed(0)

def run(commands):
    lijst = commands.split('-')

    for i in lijst:
        action = i[0]
        hoeveel = int( i[1:] )
        if action == 'F':
            turtle.forward(hoeveel)
        elif action == 'R':
            turtle.right(hoeveel)
        elif action == 'L':
            turtle.left(hoeveel)




run('F100-R90-F50-L30-F100')
turtle.done()