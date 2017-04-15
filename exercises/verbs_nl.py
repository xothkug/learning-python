klinkers = ['a', 'e', 'i', 'o', 'u']

werkwoord = "schilderen"
# todo: goochelen & schilderen, slaan, doen, rusten & blaten, opstaan

print('Het werkwoord is', werkwoord)

# de stam
# zie regels op https://www.taal-oefenen.nl/instruction/taal/werkwoorden/de-werkwoordstam/de-werkwoordstam-stamregels-1-tot-en-met-5

if werkwoord[-2:] == 'en':
    stam = werkwoord[0:-2]
elif werkwoord[-2:] == 'ën':
    stam = werkwoord[0:-2] + 'e'
else:
    stam = werkwoord[0:-1]

print('De ruwe stam is', stam)

if stam[-1] == "z":
    stam = stam[:-1] + "s"

if stam[-1] == "v":
    stam = stam[:-1] + "f"

if stam[-2] in klinkers and stam[-3] not in klinkers and stam[-1] not in klinkers:
    klinker = stam[-2]
    if klinker != 'u' or stam[-1] != 'w':
        stam = stam[:-2] + klinker + klinker + stam[-1]

if stam[-1] == stam[-2]:
    stam = stam[:-1]

print('De stam is', stam)

if werkwoord == 'skiën':
    print('Ik ski')
else:
    print(f"Ik {stam}")
print(f"Jij {stam}t")
print(f"Hij {stam}t")
print(f"Wij {werkwoord}")
print(f"Jullie {werkwoord}")
print(f"Zij {werkwoord}")
