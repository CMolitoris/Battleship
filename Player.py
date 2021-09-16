from Ship import Ship
from Grid import Grid

class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.ships = self.generate_ships()
        self.grid = Grid()
        self.grid_enemy = Grid()

    def generate_ships(self):
         list_ships = []
         list_ships.extend([Ship(2,"Destroyer"),Ship(3,"Submarine"),Ship(4,"Battleship"),Ship(4,"Battleship"),Ship(5,"Super-carrier")]) 
         return list_ships

    def place_ships(self,ship):
        #Needs to account for ship size
        self.grid.display_grid()
        location = input("Where would you like to place your " + ship.type + "? ")    
        location_split = list(location)
        letter_index = self.grid.ascii_upper.index(location_split[0])
        num_index = int(location_split[1]) - 1
        self.vert_horiz(ship,letter_index,num_index)
        self.grid.display_grid()

    def vert_horiz(self,ship,letter_index,num_index):
        growth = 0
        user_input = input("Vertical or Horizontal? (V/H) ").upper()  
        if user_input=="V":
            while growth<ship.size:
                if self.grid.matrix[num_index][letter_index] == 1:
                    print("There is a ship already occupying that position on the board.")
                    self.reset_vert(growth,num_index,letter_index)
                    self.place_ships(ship)
                else:    
                    self.grid.matrix[num_index][letter_index] = 1
                    num_index += 1
                    growth += 1
        elif user_input=="H":
            while growth<ship.size:
                if self.grid.matrix[num_index][letter_index] == 1:
                    print("There is a ship already occupying that position on the board.")
                    self.reset_horiz(growth,num_index,letter_index)
                    self.place_ships(ship)
                else:   
                    self.grid.matrix[num_index][letter_index] = 1 
                    letter_index += 1 
                    growth +=1
        else:
            self.vert_horiz()        

    def reset_vert(self,growth,num_index,letter_index):
        while growth+1>0:
            self.grid.matrix[num_index-1][letter_index] = 0
            num_index -= 1
            growth -= 1

    def reset_horiz(self,growth,num_index,letter_index):
        while growth+1>0:
            self.grid.matrix[num_index][letter_index-1] = 0
            letter_index -= 1
            growth -= 1        