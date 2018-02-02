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

