import tkinter as tk
import numpy as np

WIDTH = 5
HEIGHT = 5

class Game:
    def __init__(self):
        self.map = np.zeros((WIDTH, HEIGHT), dtype=np.int16)
        self.map[0][1] = 1
        self.map[1][1] = 1
        self.map[2][1] = 1
        self.curstep = 1

    def step(self):
        new_map = np.zeros((WIDTH, HEIGHT), dtype=np.int16)
        for yi in range(HEIGHT):
            for xi in range(WIDTH):
                value = self.map[yi][xi]
                neighbors = self.neighbors(xi, yi)
                if value == 1:
                    new_map[yi][xi] = 1 if (neighbors == 2 or neighbors == 3) else 0
                else:
                    new_map[yi][xi] = 1 if neighbors == 3 else 0
        self.map = new_map
        self.curstep += 1

    def steps(self,quantity):
        for i in range(quantity):
            self.step()

    def neighbors(self, x, y):
        count = 0
        ry = range(max(0, y - 1), 1+min(HEIGHT - 1, y + 1))
        rx = range(max(0, x - 1), 1+min(WIDTH - 1, x + 1))
        for dy in ry:
            for dx in rx:
                count += self.map[dy][dx]
        count -= self.map[x, y]
        return count

class TextRenderer:
    def render(self,map):
        for yi in range(HEIGHT):
            for xi in range(WIDTH):
                value = map[yi][xi]
                if value == 1:
                    print('1', end='')
                else:
                    print('0', end='')
            print('')
        print('')

game = Game()
textrender = TextRenderer()

game.step()
textrender.render(game.map)
game.step()
textrender.render(game.map)
