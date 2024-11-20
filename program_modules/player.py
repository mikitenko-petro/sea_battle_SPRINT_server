from .ship import Ship
from .grid import Grid

def play():
    ship_type = input("type: ")
    ship_direction = input("direction: ")
    place_row = int(input("row: "))
    place_column = int(input("column: "))

    ship = Ship(type = ship_type, direction = ship_direction, row = place_row, column = place_column)

    grid = Grid()
    grid.place_ship(ship)
    grid.show_grid()

play()