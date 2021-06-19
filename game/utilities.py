import os

def show_tab(grid):
    for i in range(len(grid)):
        if i == 2 or i == 5:
            print(f'{grid[i]}')
        else:
            print(f'{grid[i]}', end='  ')

def check_tie(count, cls, grid):
    if count == 9:
        os.system("cls")
        show_tab(grid)
        print("\nEMPATE")
        cls.tie = True