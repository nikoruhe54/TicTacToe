import Check_Board
import random

#initialize an object to check the state of the board
checkBoard = Check_Board.CheckBoard4by4()

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
        #make a random move if no winnable actions
        rand = 0
        while (rand >= 0):
            rand = random.randint(1, 16)
            if(checkBoard.game.Spaces[rand].state == 0):
                playMove(rand,"computer")
                rand = -1

    elif (skill == "beginner"):
        #beginner skill level always just makes a random move
        rand = 0
        while (rand >= 0):
            rand = random.randint(1, 9)
            if (checkBoard.game.Spaces[rand].state == 0):
                playMove(rand,"computer")
                rand = -1


def checkForDraw():
    count = 0
    for i in range(1,17):
        if (checkBoard.game.Spaces[i].state != 0):
            count += 1
    if (count == 16):
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
        for x in range(1,17):
            if (position != x):
                errorCheck += 1
        if (errorCheck > 15):
            print("Not a valid input. Pick a space (1-16)")
            return -1
        if(checkBoard.game.Spaces[position].state == 0):
            checkBoard.game.Spaces[position].state = 10
            print(player + " took space: ")
            print(position)
            return 0
        else:
            print("Sorry, that space is already taken. Pick another")
            return -1

def takeAction(target):
    if(target == "top row"):
        for i in range (1,5):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
    elif(target == "second row"):
        for i in range (5,9):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
    elif(target == "third row"):
        for i in range (9,13):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
    elif(target == "last row"):
        for i in range (13,17):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
    elif(target == "first column"):
        i = 1
        while (i < 14):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 4
    elif(target == "second column"):
        i = 2
        while (i < 15):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 4
    elif(target == "third column"):
        i = 3
        while (i < 16):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 4
    elif(target == "last column"):
        i = 4
        while (i < 17):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 4
    elif(target == "down diagnol"):
        i = 1
        while (i < 17):
            if (checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 5
    elif(target == "up diagnol"):
        i = 4
        while (i < 14):
            if(checkBoard.game.Spaces[i].state == 0):
                playMove(i, "computer")
            i = i + 3

def resetGame():
    for x in range(1, 17):
        checkBoard.game.Spaces[x].state = 0
        checkBoard.game.Spaces[x].state = 0