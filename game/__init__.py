from game.utilities import show_tab
import os

class Player:

    tie = False

    def __init__(self, name, draw, victory = False):
        self.name = name
        self.draw = draw
        self.victory = victory

    def get_pos(self):
        return int(input(f"\nEm qual posição deseja botar o {self.draw}? "))

    def addDraw(self, grid):
        pos = self.get_pos()
        grid[pos-1] = self.draw

    def check_win(self, grid):
        if grid[0] == grid[1] == grid[2] or grid[3] == grid[4] == grid[5] or grid[6] == grid[7] == grid[8] or grid[0] == grid[3] == grid[6] or grid[1] == grid[4] == grid[7] or grid[2] == grid[5] == grid[8] or grid[0] == grid[4] == grid[8] or grid[2] == grid[4] == grid[6]:
            if '1' in self.name:
                os.system("cls")
                show_tab(grid)
                print(f"\nVITÓRIA DO JOGADOR 1")
            else:
                os.system("cls")
                show_tab(grid)
                print(f"\nVITÓRIA DO JOGADOR 2")
            self.victory = True


class Bot:
    pass