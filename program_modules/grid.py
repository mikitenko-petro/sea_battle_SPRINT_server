class Grid():
    def __init__(self):
        self.grid = [
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        ]

    def place_ship(self, ship):
        if ship.row - 1 > -1 and  ship.column - 1 > -1:
            if ship.type == "1":
                self.grid[ship.row - 1][ship.column - 1] = "X"

            elif ship.type == "2":
                if ship.direction == "top":
                    if ship.row - 2> -1 and  ship.column - 1 > -1:
                        self.grid[ship.row - 1][ship.column - 1] = "X"
                        self.grid[ship.row - 2][ship.column - 1] = "x"
                    else:
                        self.say_error()

                elif ship.direction == "right":
                    if ship.row - 1 > -1 and  ship.column > -1:
                        self.grid[ship.row - 1][ship.column - 1] = "X"
                        self.grid[ship.row - 1][ship.column] = "x"
                    else:
                        self.say_error()

                elif ship.direction == "bottom":
                    if ship.row > -1 and  ship.column > -1:
                        self.grid[ship.row - 1][ship.column - 1] = "X"
                        self.grid[ship.row][ship.column - 1] = "x"
                    else:
                        self.say_error()

                elif ship.direction == "left":
                    if ship.row - 1 > -1 and  ship.column - 2> -1:
                        self.grid[ship.row - 1][ship.column - 1] = "X"
                        self.grid[ship.row - 1][ship.column - 2] = "x"
                    else:
                        self.say_error()
                        
        else:
            self.say_error()

    def show_grid(self):
        for row in self.grid:
            print(row)

    def say_error(self):
            print("wrong plasement")

