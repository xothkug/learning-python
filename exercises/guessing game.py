import random

raad_cijfer = random.randint(1, 300)

while True:
    cijfer = int(input('Raad het cijfer tussen 1-300 '))

    if cijfer < raad_cijfer:
        print('hoger')
    elif cijfer > raad_cijfer:
        print('lager')
    else:
        break;

print('ok')
