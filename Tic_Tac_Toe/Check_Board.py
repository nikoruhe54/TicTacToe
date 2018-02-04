import Game_Board

class CheckBoard:

    def __init__(self):
        self.game = Game_Board.Board()

    def checkBestOption(self, position):
        #determine where the best move is when there are no obvious moves
        count = 0
        if(position == 1):
            if(self.game.Spaces[2].state + self.game.Spaces[3].state == 1):
                count += 1
            if(self.game.Spaces[4].state + self.game.Spaces[7].state == 1):
                count += 1
            if(self.game.Spaces[5].state + self.game.Spaces[9].state == 1):
                count += 1
        elif(position == 2):
            if(self.game.Spaces[1].state + self.game.Spaces[3].state == 1):
                count +=1
            if(self.game.Spaces[5].state + self.game.Spaces[8].state == 1):
                count += 1
        elif(position == 3):
            if(self.game.Spaces[1].state + self.game.Spaces[2].state == 1):
                count += 1
            if(self.game.Spaces[6].state + self.game.Spaces[9].state == 1):
                count += 1
            if(self.game.Spaces[5].state + self.game.Spaces[7].state == 1):
                count += 1
        elif(position == 4):
            if(self.game.Spaces[5].state + self.game.Spaces[6].state == 1):
                count +=1
            if(self.game.Spaces[1].state + self.game.Spaces[7].state == 1):
                count += 1
        elif (position == 5):
            if(self.game.Spaces[4].state + self.game.Spaces[6].state == 1):
                count += 1
            if(self.game.Spaces[2].state + self.game.Spaces[8].state == 1):
                count += 1
            if(self.game.Spaces[1].state + self.game.Spaces[9].state == 1):
                count += 1
            if(self.game.Spaces[3].state + self.game.Spaces[7].state == 1):
                count += 1

    def tryToWin(self):
        #check for all 8 possible winning outcomes
        if(self.game.Spaces[1].state + self.game.Spaces[2].state + self.game.Spaces[3].state == 2):
            return("top row")
        elif(self.game.Spaces[4].state + self.game.Spaces[5].state + self.game.Spaces[6].state == 2):
            return("middle row")
        elif(self.game.Spaces[7].state + self.game.Spaces[8].state + self.game.Spaces[9].state == 2):
            return("bottom row")
        elif(self.game.Spaces[1].state + self.game.Spaces[4].state + self.game.Spaces[7].state == 2):
            return("left column")
        elif(self.game.Spaces[2].state + self.game.Spaces[5].state + self.game.Spaces[8].state == 2):
            return("middle column")
        elif(self.game.Spaces[3].state + self.game.Spaces[6].state + self.game.Spaces[9].state == 2):
            return("right column")
        elif(self.game.Spaces[1].state + self.game.Spaces[5].state + self.game.Spaces[9].state == 2):
            return("down diagnol")
        elif(self.game.Spaces[3].state + self.game.Spaces[5].state + self.game.Spaces[7].state == 2):
            return("up diagnol")
        else:
            return("none")


    def checkOpponent(self):
        #check to see if the opponent has two in a row
        if(self.game.Spaces[1].state + self.game.Spaces[2].state + self.game.Spaces[3].state == 20):
            return("top row")
        elif(self.game.Spaces[4].state + self.game.Spaces[5].state + self.game.Spaces[6].state == 20):
            return("middle row")
        elif(self.game.Spaces[7].state + self.game.Spaces[8].state + self.game.Spaces[9].state == 20):
            return("bottom row")
        elif(self.game.Spaces[1].state + self.game.Spaces[4].state + self.game.Spaces[7].state == 20):
            return("left column")
        elif(self.game.Spaces[2].state + self.game.Spaces[5].state + self.game.Spaces[8].state == 20):
            return("middle column")
        elif(self.game.Spaces[3].state + self.game.Spaces[6].state + self.game.Spaces[9].state == 20):
            return("right column")
        elif(self.game.Spaces[1].state + self.game.Spaces[5].state + self.game.Spaces[9].state == 20):
            return("down diagnol")
        elif(self.game.Spaces[3].state + self.game.Spaces[5].state + self.game.Spaces[7].state == 20):
            return("up diagnol")
        else:
            return("none")

    def checkForWin(self):
        #check to see if the computer has won
        if(self.game.Spaces[1].state + self.game.Spaces[2].state + self.game.Spaces[3].state == 3):
            return(1)
        elif(self.game.Spaces[4].state + self.game.Spaces[5].state + self.game.Spaces[6].state == 3):
            return(1)
        elif(self.game.Spaces[7].state + self.game.Spaces[8].state + self.game.Spaces[9].state == 3):
            return(1)
        elif(self.game.Spaces[1].state + self.game.Spaces[4].state + self.game.Spaces[7].state == 3):
            return(1)
        elif(self.game.Spaces[2].state + self.game.Spaces[5].state + self.game.Spaces[8].state == 3):
            return(1)
        elif(self.game.Spaces[3].state + self.game.Spaces[6].state + self.game.Spaces[9].state == 3):
            return(1)
        elif(self.game.Spaces[1].state + self.game.Spaces[5].state + self.game.Spaces[9].state == 3):
            return(1)
        elif(self.game.Spaces[3].state + self.game.Spaces[5].state + self.game.Spaces[7].state == 3):
            return(1)
        #check to see if the human player has won
        if(self.game.Spaces[1].state + self.game.Spaces[2].state + self.game.Spaces[3].state == 30):
            return(-1)
        elif(self.game.Spaces[4].state + self.game.Spaces[5].state + self.game.Spaces[6].state == 30):
            return(-1)
        elif(self.game.Spaces[7].state + self.game.Spaces[8].state + self.game.Spaces[9].state == 30):
            return(-1)
        elif(self.game.Spaces[1].state + self.game.Spaces[4].state + self.game.Spaces[7].state == 30):
            return(-1)
        elif(self.game.Spaces[2].state + self.game.Spaces[5].state + self.game.Spaces[8].state == 30):
            return(-1)
        elif(self.game.Spaces[3].state + self.game.Spaces[6].state + self.game.Spaces[9].state == 30):
            return(-1)
        elif(self.game.Spaces[1].state + self.game.Spaces[5].state + self.game.Spaces[9].state == 30):
            return(-1)
        elif(self.game.Spaces[3].state + self.game.Spaces[5].state + self.game.Spaces[7].state == 30):
            return(-1)
        else:
            return(0)

