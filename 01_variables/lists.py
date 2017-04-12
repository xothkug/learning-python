games = ['Minecraft', 'Age Of Empires', 'Terraria', 'Agario']
colors = ['red', 'green', 'blue', 'yellow']

print(games[0])
print(games[-1])
print(games[0:3])
print(games + colors)
print(games[1:2] + colors[2:3])  # list + list
print(games[1] + colors[2])  # string + string

colors.append('black')
print(colors)

colors[0:2] = ['r', 'g']
print(colors)

print(len(colors))



