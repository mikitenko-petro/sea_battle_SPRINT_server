from .grid import Grid
from .ship import Ship
from .client import client

def play():
    client()
    player_sea = Grid()
    enemy_sea = Grid()
    
    while True:
        type = input("type: ")
        direction = input("direction: ")
        row = int(input("row: ")) 
        column = int(input("collum: "))

        ship = Ship(type = type, direction = direction, row = row, column = column)
 
        player_sea.place_ship(ship = ship)

        print("player grid")
        player_sea.show_grid()

        print("enemy grid")
        enemy_sea.show_grid()

         

play()