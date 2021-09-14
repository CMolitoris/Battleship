from Ship import Ship
from Grid import Grid

class Player:
    def __init__(self) -> None:
        self.ships = self.generate_ships()
        self.grid = Grid()
        self.grid_enemy = Grid()

    def generate_ships(self):
         list_ships = []
         list_ships.extend([Ship(2,"Destroyer"),Ship(3,"Submarine"),Ship(4,"Battleship"),Ship(4,"Battleship"),Ship(5,"Super-carrier")]) 
         return list_ships

    def place_ships(self,ship):
        #Needs to account for ship size
        location = input("Where would you like to place your " + ship.type + "? ")    
        location_split = list(location)
        letter_index = self.grid.ascii_upper.index(location_split[0])
        num_index = int(location_split[1]) - 1
        self.grid.matrix[letter_index][num_index] = 1
        self.grid.display_grid()