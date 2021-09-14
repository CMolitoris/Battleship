import string

class Grid:
    def __init__(self) -> None:
        self.matrix = self.initialize_grid()
        self.ascii_upper = self.populate_letters()

    def initialize_grid(self):
        rows, cols =  (20,20)  
        return [[0]*cols]*rows

    def display_grid(self):
        count = 0
        print()
        # for n in range(19):
        #     print(self.ascii_upper[n],end="  ")
        # print()   
        self.print_top_index()

        for m in self.matrix:
            for n in m:
                if count==19:
                    count=0
                    print()
                else:  
                    print(n,end="  ")
                    count += 1 
        print()             
            
    def populate_letters(self):
        letter_list = []
        for n in string.ascii_uppercase:
            letter_list.append(n)
        return letter_list   

    def print_top_index(self):
        str_letters = ""
        for i in range(19):
            str_letters += self.ascii_upper[i] + "  "    
        print('\33[35m' + str_letters + '\33[0m')    