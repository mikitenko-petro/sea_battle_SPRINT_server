import threading
from .ship import Ship
from .grid import Grid
from .server import client, client2, which, start_server

def play(grid_place):
    #ship_type = input("type: ")
    #ship_direction = input("direction: ")
    #place_row = int(input("row: "))
    #place_column = int(input("column: "))

    #ship = Ship(type = ship_type, direction = ship_direction, row = place_row, column = place_column)

    server = threading.Thread(target= start_server())
    grid = threading.Thread(Grid(target= grid_place))
    grid_placing = threading.Thread(target= grid.show_grid(grid_place))
    #grid.place_ship(ship)

    server.start()
    grid.start()
    grid_placing.start()
    if which == 1:
        play(client)
    if which == 2:
        play(client2)
    print("Усьо ок усьо вместе брат, брат брату")