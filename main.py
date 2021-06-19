import os
from game import *
from game.utilities import *

p1 = Player('p1', 'X')
p2 = Player('p2', 'O')

def main():
    
    tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    rounds = 1
    
    while p1.victory == False and p2.victory == False and Player.tie == False:
        os.system("cls")
        show_tab(tab)
        if rounds % 2 != 0:
            p1.addDraw(tab)
            p1.check_win(tab)
        else:
            p2.addDraw(tab)
            p2.check_win(tab)
        
        
        check_tie(rounds, Player, tab)
        rounds += 1

main()