#Niko Ruhe
#AI Class
#University of Akron
#Dr. Chan
#02/18/2018

import Space_State

class Board:

    def __init__(self):
        self.Spaces = [0 for i in range(10)]

        for x in range(1 , 10):
            if(x % 2 == 1 and x != 5):
                self.Spaces[x] = Space_State.Space(0,3)
            elif(x % 2 == 0):
                self.Spaces[x] = Space_State.Space(0,2)
            else:
                self.Spaces[x] = Space_State.Space(0,4)


class Board4x4:

    def __init__(self):
        self.Spaces = [0 for i in range(17)]
        for x in range(1, 17):
            if(x == 1 or x == 4 or x == 13 or x == 16 or x == 6 or
               x == 7 or x == 10 or x == 11):
                self.Spaces[x] = Space_State.Space(0,3)
            elif(x == 2 or x == 3 or x == 5 or x == 8 or x == 9 or
                 x == 12 or x == 14 or x == 15):
                self.Spaces[x] = Space_State.Space(0,2)
