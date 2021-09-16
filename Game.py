from io import SEEK_SET
from Player import Player


from Player import Player

class Game:
    def __init__(self) -> None:
        self.player_one = Player("Player One")
        self.player_two = Player("Player Two")
        self.play_game()

    def play_game(self):
        self.ship_placement(self.player_one)
        self.ship_placement(self.player_two)

    def ship_placement(self,player):
        count = 0
        track_list = []
        used = True
        print("\n" + player.name + "'s turn to place ships!\n")
        ships = player.generate_ships()
        while count<5:
            choice = self.display_ships(ships)
            if choice==1:
                count = self.validate_placement(player,ships,choice,track_list,count,0)   

            elif choice==2:
                count = self.validate_placement(player,ships,choice,track_list,count,1)
            
            elif choice==3: 
                count = self.validate_placement(player,ships,choice,track_list,count,2)
            
            elif choice==4:
                count = self.validate_placement(player,ships,choice,track_list,count,3)
            
            elif choice==5:
                count = self.validate_placement(player,ships,choice,track_list,count,4)

    def validate_placement(self,player,ships,choice,track_list,count,index):
        used = self.check_entry(track_list,choice)
        if used == True:
            player.place_ships(player.ships[index])
            ships[index].type += " (PLACED)"
            track_list.append(choice)
            return count + 1
        else:
            print("You already placed this ship\n")  
            return count               

    def check_entry(self,list,choice):
        if choice in list:
            return False
        return True    
        

    def display_ships(self,ships):
        count = 1
        for n in ships:
            print(str(count) + ": " + n.type)
            count += 1
        print()    
        return int(input("Which ship would you like to place? "))