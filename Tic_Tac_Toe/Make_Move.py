import Check_Board
import random

#initialize an object to check the state of the board
checkBoard = Check_Board.CheckBoard()

#high level logic for a computer move
def makeComputerMove(skill, order):
    if (skill == "expert"):
        #win the game if possible
        check = checkBoard.tryToWin()
        if (check != "none"):
            takeAction(check)
            return(0)
        else:
            #block opponent from winning the game if possible
            check = checkBoard.checkOpponent()
            if (check != "none"):
                takeAction(check)
                return(0)

        #play into the future
        #see if computer can make a move to guarantee victory later
        SpaceCount = 0
        for y in range(1, 10):
            SpaceCount += checkBoard.game.Spaces[y].state
        if (SpaceCount > 21):
            tryToWin = predictWinMove(1)
            if (tryToWin > 0):
                playMove(tryToWin,"computer")
                return(0)
            #see if human can make a move to guarantee victory later, and block it
            tryToWin = predictWinMove(10)
            if (tryToWin > 0):
                playMove(tryToWin,"computer")
                return(0)
        #if winning and blocking the opponent are not possible, make a strategic move
        scanForBestMove(order)
    elif (skill == "beginner"):
        #beginner skill level always just makes a random move
        rand = 0
        while (rand >= 0):
            rand = random.randint(1, 9)
            if (checkBoard.game.Spaces[rand].state == 0):
                playMove(rand,"computer")
                rand = -1

def predictWinMove(i):
    #what moves will lead to a winnable outcome
    #return the intersection number

    #start with those at space 1
    if(checkBoard.game.Spaces[1].state + checkBoard.game.Spaces[2].state + checkBoard.game.Spaces[3].state +
        checkBoard.game.Spaces[4].state + checkBoard.game.Spaces[7].state == 2*i):
        return 1
    #2nd space
    elif(checkBoard.game.Spaces[2].state + checkBoard.game.Spaces[1].state + checkBoard.game.Spaces[3].state +
       checkBoard.game.Spaces[5].state + checkBoard.game.Spaces[8].state == 2*i):
        return 2
    #3rd space
    elif(checkBoard.game.Spaces[3].state + checkBoard.game.Spaces[1].state + checkBoard.game.Spaces[2].state +
       checkBoard.game.Spaces[6].state + checkBoard.game.Spaces[9].state == 2*i):
        return 3
    #4th space
    elif(checkBoard.game.Spaces[4].state + checkBoard.game.Spaces[5].state + checkBoard.game.Spaces[6].state +
       checkBoard.game.Spaces[1].state + checkBoard.game.Spaces[7].state == 2*i):
        return 4
    #5th space
    elif(checkBoard.game.Spaces[5].state + checkBoard.game.Spaces[4].state + checkBoard.game.Spaces[6].state +
       checkBoard.game.Spaces[2].state + checkBoard.game.Spaces[8].state == 2*i):
        return 5
    #6th space
    elif(checkBoard.game.Spaces[6].state + checkBoard.game.Spaces[4].state + checkBoard.game.Spaces[5].state +
       checkBoard.game.Spaces[3].state + checkBoard.game.Spaces[9].state == 2*i):
        return 6
    #7th space
    elif(checkBoard.game.Spaces[7].state + checkBoard.game.Spaces[8].state + checkBoard.game.Spaces[9].state +
       checkBoard.game.Spaces[1].state + checkBoard.game.Spaces[4].state == 2*i):
        return 7
    #8th space
    elif(checkBoard.game.Spaces[8].state + checkBoard.game.Spaces[7].state + checkBoard.game.Spaces[9].state +
       checkBoard.game.Spaces[2].state + checkBoard.game.Spaces[5].state == 2*i):
        return 8
    #9th space
    elif(checkBoard.game.Spaces[9].state + checkBoard.game.Spaces[7].state + checkBoard.game.Spaces[8].state +
       checkBoard.game.Spaces[3].state + checkBoard.game.Spaces[6].state == 2*i):
        return 9
    #diagnols
    elif(checkBoard.game.Spaces[1].state + checkBoard.game.Spaces[3].state + checkBoard.game.Spaces[5].state +
       checkBoard.game.Spaces[7].state + checkBoard.game.Spaces[9].state == 2*i):
        return 5
    else:
        return 0
#identify the best space to take when no winning moves occur
def scanForBestMove(turn):
    #store the states of which space is best
    slot = -1
    winningMoves = 0
    #figure out which space has the greatest amount of winnable states
    updateWinningMoves()

    SpaceCount = 0
    for y in range(1,10):
        SpaceCount += checkBoard.game.Spaces[y].state
    if ((SpaceCount < 21 and turn == "second") or (SpaceCount < 22 and turn == "first")):
        for i in range(1,10):
            #keep spaces that have higher win counts
            if(checkBoard.game.Spaces[i].state == 0 and checkBoard.game.Spaces[i].winMoves >= winningMoves):
                if (checkBoard.game.Spaces[i].winMoves > winningMoves):
                    slot = i
                winningMoves = checkBoard.game.Spaces[i].winMoves
                #in the case of a tie
                #if the first slot is unoccupied, take it
                if (slot == -1):
                    slot = i
                #then take the odd slots (corners and center)
                elif (i % 2 == 1 and slot != 5):
                    slot = i
                #give highest priority to the center slot
                if (i % 5 == 0):
                    slot = i
    else:
        #two moves have already been made, move into traffic
        winningMoves = 4
        for i in range(1,10):
            #keep spaces that have lower win counts
            if(checkBoard.game.Spaces[i].state == 0 and checkBoard.game.Spaces[i].winMoves <= winningMoves):
                if (checkBoard.game.Spaces[i].winMoves < winningMoves):
                    slot = i
                winningMoves = checkBoard.game.Spaces[i].winMoves
                #in the case of a tie
                #if the first slot is unoccuppied, take it
                if (slot == -1):
                    slot = i
                #then take the even slots
                elif (i % 2 == 0):
                    slot = i
                #give higheest priority to the center slot
                elif (i % 5 == 0):
                    slot = i

    #play the move
    playMove(slot, "computer")

def checkForDraw():
    count = 0
    for i in range(1,10):
        if (checkBoard.game.Spaces[i].state != 0):
            count += 1
    if (count == 9):
        return 1
    else:
        return 0

def playMove(position, player):

    if(player == "computer"):
        checkBoard.game.Spaces[position].state = 1
        print(player + " took space: ")
        print (position)
        return 0
    elif(player == "human"):
        errorCheck = 0
        for x in range(1,10):
            if (position != x):
                errorCheck += 1
        if (errorCheck > 8):
            print("Not a valid input. Pick a space (1-9)")
            return -1
        if(checkBoard.game.Spaces[position].state == 0):
            checkBoard.game.Spaces[position].state = 10
            print(player + " took space: ")
            print(position)
            return 0
        else:
            print("Sorry, that space is already taken. Pick another")
            return -1

def updateWinningMoves():
    #reset all the winning moves
    for x in range(1, 10):
        if (x % 2 == 1 and x != 5):
            checkBoard.game.Spaces[x].winMoves = 3
        elif (x % 2 == 0):
            checkBoard.game.Spaces[x].winMoves = 2
        else:
            checkBoard.game.Spaces[x].winMoves = 4

     #check to see if the human took space 1
    if (checkBoard.game.Spaces[1].state == 10):
        for y in range(1, 10):
            checkBoard.game.Spaces[y].winMoves -= 1
        checkBoard.game.Spaces[6].winMoves += 1
        checkBoard.game.Spaces[8].winMoves += 1

    #check to see if the human took space 2
    if (checkBoard.game.Spaces[2].state == 10):
        for y in range(1, 10):
            checkBoard.game.Spaces[y].winMoves -= 1
        checkBoard.game.Spaces[4].winMoves += 1
        checkBoard.game.Spaces[6].winMoves += 1
        checkBoard.game.Spaces[7].winMoves += 1
        checkBoard.game.Spaces[9].winMoves += 1

    #check to see if the human took space 3
    if (checkBoard.game.Spaces[3].state == 10):
        for y in range(1, 10):
            checkBoard.game.Spaces[y].winMoves -= 1
        checkBoard.game.Spaces[4].winMoves += 1
        checkBoard.game.Spaces[8].winMoves += 1

    #check to see if the human took space 4
    if (checkBoard.game.Spaces[4].state == 10):
        for y in range(1, 10):
            checkBoard.game.Spaces[y].winMoves -= 1
        checkBoard.game.Spaces[2].winMoves += 1
        checkBoard.game.Spaces[3].winMoves += 1
        checkBoard.game.Spaces[8].winMoves += 1
        checkBoard.game.Spaces[9].winMoves += 1

    #check to see if the human took space 5
    if (checkBoard.game.Spaces[5].state == 10):
        for y in range(1, 10):
            checkBoard.game.Spaces[y].winMoves -= 1

    #check to see if the human took space 6
    if (checkBoard.game.Spaces[6].state == 10):
        for y in range(1, 10):
            checkBoard.game.Spaces[y].winMoves -= 1
        checkBoard.game.Spaces[1].winMoves += 1
        checkBoard.game.Spaces[2].winMoves += 1
        checkBoard.game.Spaces[7].winMoves += 1
        checkBoard.game.Spaces[8].winMoves += 1

    #check to see if the human took space 7
    if (checkBoard.game.Spaces[7].state == 10):
        for y in range(1, 10):
            checkBoard.game.Spaces[y].winMoves -= 1
        checkBoard.game.Spaces[2].winMoves += 1
        checkBoard.game.Spaces[6].winMoves += 1

    #check to see if the human took space 8
    if (checkBoard.game.Spaces[8].state == 10):
        for y in range(1, 10):
            checkBoard.game.Spaces[y].winMoves -= 1
        checkBoard.game.Spaces[1].winMoves += 1
        checkBoard.game.Spaces[3].winMoves += 1
        checkBoard.game.Spaces[4].winMoves += 1
        checkBoard.game.Spaces[6].winMoves += 1

    #check to see if the human took space 9
    if (checkBoard.game.Spaces[9].state == 10):
        for y in range(1, 10):
            checkBoard.game.Spaces[y].winMoves -= 1
        checkBoard.game.Spaces[2].winMoves += 1
        checkBoard.game.Spaces[4].winMoves += 1


def takeAction(target):
    if(target == "top row"):
        for i in range (1,4):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
    elif(target == "middle row"):
        for i in range (4,7):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
    elif(target == "bottom row"):
        for i in range (7,10):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
    elif(target == "left column"):
        i = 1
        while (i < 8):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 3
    elif(target == "middle column"):
        i = 2
        while (i < 9):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 3
    elif(target == "right column"):
        i = 3
        while (i < 10):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 3
    elif(target == "down diagnol"):
        i = 1
        while (i < 10):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 4
    elif(target == "up diagnol"):
        i = 3
        while (i < 8):
            if(checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 2


def resetGame():
    for x in range(1, 10):
        checkBoard.game.Spaces[x].state = 0
        if (x % 2 == 1 and x != 5):
            checkBoard.game.Spaces[x].winMoves = 3
        elif (x % 2 == 0):
            checkBoard.game.Spaces[x].winMoves = 2
        else:
            checkBoard.game.Spaces[x].winMoves = 4