import Game_Board

class CheckBoard:

    def __init__(self):
        self.game = Game_Board.Board()


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
            print("game over, computer wins")
            return(1)
        elif(self.game.Spaces[4].state + self.game.Spaces[5].state + self.game.Spaces[6].state == 3):
            print("game over, computer wins")
            return(1)
        elif(self.game.Spaces[7].state + self.game.Spaces[8].state + self.game.Spaces[9].state == 3):
            print("game over, computer wins")
            return(1)
        elif(self.game.Spaces[1].state + self.game.Spaces[4].state + self.game.Spaces[7].state == 3):
            print("game over, computer wins")
            return(1)
        elif(self.game.Spaces[2].state + self.game.Spaces[5].state + self.game.Spaces[8].state == 3):
            print("game over, computer wins")
            return(1)
        elif(self.game.Spaces[3].state + self.game.Spaces[6].state + self.game.Spaces[9].state == 3):
            print("game over, computer wins")
            return(1)
        elif(self.game.Spaces[1].state + self.game.Spaces[5].state + self.game.Spaces[9].state == 3):
            print("game over, computer wins")
            return(1)
        elif(self.game.Spaces[3].state + self.game.Spaces[5].state + self.game.Spaces[7].state == 3):
            print("game over, computer wins")
            return(1)
        #check to see if the human player has won
        if(self.game.Spaces[1].state + self.game.Spaces[2].state + self.game.Spaces[3].state == 30):
            print("game over, human wins")
            return(-1)
        elif(self.game.Spaces[4].state + self.game.Spaces[5].state + self.game.Spaces[6].state == 30):
            print("game over, human wins")
            return(-1)
        elif(self.game.Spaces[7].state + self.game.Spaces[8].state + self.game.Spaces[9].state == 30):
            print("game over, human wins")
            return(-1)
        elif(self.game.Spaces[1].state + self.game.Spaces[4].state + self.game.Spaces[7].state == 30):
            print("game over, human wins")
            return(-1)
        elif(self.game.Spaces[2].state + self.game.Spaces[5].state + self.game.Spaces[8].state == 30):
            print("game over, human wins")
            return(-1)
        elif(self.game.Spaces[3].state + self.game.Spaces[6].state + self.game.Spaces[9].state == 30):
            print("game over, human wins")
            return(-1)
        elif(self.game.Spaces[1].state + self.game.Spaces[5].state + self.game.Spaces[9].state == 30):
            print("game over, human wins")
            return(-1)
        elif(self.game.Spaces[3].state + self.game.Spaces[5].state + self.game.Spaces[7].state == 30):
            print("game over, human wins")
            return(-1)
        else:
            return(0)

    def resetGame(self):
        for i in range (1,10):
            self.game.Spaces[i].state = 0
            self.game.Spaces[i].state = 0