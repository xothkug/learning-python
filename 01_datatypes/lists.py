games = ['Minecraft', 'Age Of Empires', 'Terraria', 'Agario']
colors = ['red', 'green', 'blue', 'yellow']
numbers = [10, 20, 50]

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

games_and_colors = games + colors

print(games_and_colors)

one_to_ten = range(1, 11)
print(one_to_ten)

games.remove('Minecraft')
print(games)


