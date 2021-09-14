import string

class Grid:
    def __init__(self) -> None:
        self.matrix = self.initialize_grid()
        self.ascii_upper = self.populate_letters()

    def initialize_grid(self):
        rows, cols =  20,20  
        return [[0 for x in range(rows)] for y in range(cols)]

    def display_grid(self):
        count = 0
        count_left_index = 1
        print()  
        self.print_top_index()

        for m in self.matrix:
            if count_left_index<10:
                count_color = ""
                count_color += '\33[34m' + str(count_left_index) + '\33[0m' 
                print(count_color,end="   ")
            else:  
                count_color = ""
                count_color += '\33[34m' + str(count_left_index) + '\33[0m'  
                print(count_color,end="  ")

            for n in m:
                if count==19:
                    count=0
                    print()
                elif n==1:
                    color_int = '\33[31m' + "1" + '\33[0m'
                    print(color_int,end="  ")
                    count += 1 
                else:  
                    print(n,end="  ")
                    count += 1 
            count_left_index += 1            
        print()             
            
    def populate_letters(self):
        letter_list = []
        for n in string.ascii_uppercase:
            letter_list.append(n)
        return letter_list   

    def print_top_index(self):
        str_letters = "  "
        for i in range(19):
            str_letters += "  " + self.ascii_upper[i]     
        print('\33[34m' + str_letters + '\33[0m')    