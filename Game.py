from io import SEEK_SET
from Player import Player


from Player import Player

class Game:
    def __init__(self) -> None:
        self.player_one = Player()
        self.player_two = Player()

    def play_game(self):
        self.ship_placement(self.player_one)
        self.ship_placement(self.player_two)

    def ship_placement(self,player):
        ships = self.player.generate_ships()
        while len(ships)!=0:
            choice = self.display_ships(ships)
            if choice==1:
                self.player.place_ships(ships[0])
                ships.remove(ships[0])
            elif choice==2:
                self.player.place_ships(ships[1])
                ships.remove(ships[0])
            elif choice==3: 
                self.player.place_ships(ships[2])
                ships.remove(ships[0])
            elif choice==4:
                self.player.place_ships(ships[3])
                ships.remove(ships[0])
            elif choice==5:
                self.player.place_ships(ships[4])            
                ships.remove(ships[0])

        

    def display_ships(self,ships):
        count = 1
        for n in ships:
            print(count + ": " + n.name)
            count += 1
        print()    
        return int(input("Which ship would you like to place? "))