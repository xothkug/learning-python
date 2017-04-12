getal = 1

while True:

    priem = True

    for i in range(2,getal):
        if getal % i == 0:
            priem = False
            break

    if priem:
        print(getal)

    getal = getal + 1
