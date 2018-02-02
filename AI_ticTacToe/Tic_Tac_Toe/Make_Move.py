import Check_Board

checkBoard = Check_Board.CheckBoard()

def makeComputerMove():
    check = checkBoard.tryToWin()
    if (check != "none"):
        makeWinningMove(check)
        return(0)
    else:
        check = checkBoard.checkOpponent()
        if (check != "none"):
            blockOpponent(check)
            return(0)
    if (checkBoard.checkForWin() == 0):
        scanForBestMove()

def scanForBestMove():
    slot = -1
    winningMoves = 0
    updateWinningMoves()
    for i in range(1,10):
        if(checkBoard.game.Spaces[i].state == 0 and checkBoard.game.Spaces[i].winMoves >= winningMoves):
            winningMoves = checkBoard.game.Spaces[i].winMoves
            slot = i
    if(slot == -1):
        for j in range(1,10):
            if(checkBoard.game.Spaces[j].state == 0):
                slot = j
    playMove(slot, "computer")

def playMove(position, player):

    if(player == "computer"):
        checkBoard.game.Spaces[position].state = 1
    if(player == "human"):
        checkBoard.game.Spaces[position].state = 10

    print(player + " took space: ")
    print(position)
    checkBoard.checkForWin()

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


def blockOpponent(target):
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

def makeWinningMove(target):
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