import Make_Move
import Draw_Board

#main function loop that walks the players through the game
def Play(level, humanTurn):
    #start by drawing the empty board and identifying the options the player selected
    Draw_Board.drawBoard()

    if (humanTurn == "first" and Level == "easy"):
        #after every turn, check to see if a player won
        while (Make_Move.checkBoard.checkForWin() == 0):
            #user error checking implementation
            validMove = -1
            while (validMove == -1):
                try:
                    #user enters an integer for the move and make sure the move is valid
                    YourMove = input("What move would you like to make? (1-9)")
                    validMove = Make_Move.playMove(YourMove, "human")
                    Draw_Board.drawBoard()
                except:
                    print("could not recognize space")
            #see if the player made a move that results in a draw
            if(Make_Move.checkForDraw() == 1):
                break
            #check to see if the game has been won
            if(Make_Move.checkBoard.checkForWin() == 0):
                #make the computer move
                Make_Move.makeComputerMove(Level, humanTurn)
                Draw_Board.drawBoard()
            if(Make_Move.checkForDraw() == 1):
                break
        #a win has been detected, figure out who won
        if(Make_Move.checkBoard.checkForWin() == 1):
            print("Computer Wins")
        elif(Make_Move.checkBoard.checkForWin() == -1):
            print("Human Wins")
        else:
            print("The game is a draw")

    #check the next set of option selected by the user and play the game
    elif (humanTurn == "second" and Level == "easy"):
        #check to see if anyone has won
        while (Make_Move.checkBoard.checkForWin() == 0):
            #make the computer play a move
            Make_Move.makeComputerMove(Level, humanTurn)
            Draw_Board.drawBoard()
            if(Make_Move.checkForDraw() == 1):
                break
            if(Make_Move.checkBoard.checkForWin() == 0):
                #error detection
                validMove = -1
                while (validMove == -1):
                    try:
                        #make the human move
                        YourMove = input("What move would you like to make? (1-9)")
                        validMove = Make_Move.playMove(YourMove, "human")
                        Draw_Board.drawBoard()
                    except:
                        print("could not recognize space")
            if(Make_Move.checkForDraw() == 1):
                break
        #determine who has won
        if(Make_Move.checkBoard.checkForWin() == 1):
            print("Computer Wins")
        elif(Make_Move.checkBoard.checkForWin() == -1):
            print("HumanWins")
        else:
            print("The game is a draw")

    #test the next set of options
    elif (humanTurn == "first" and Level == "hard"):
        while (Make_Move.checkBoard.checkForWin() == 0):
            #error handling
            validMove = -1
            while (validMove == -1):
                try:
                    #make human move
                    YourMove = input("What move would you like to make? (1-9)")
                    validMove = Make_Move.playMove(YourMove, "human")
                    Draw_Board.drawBoard()
                except:
                    print("could not recognize space")
            if(Make_Move.checkForDraw() == 1):
                break
            if(Make_Move.checkBoard.checkForWin() == 0):
                #make the computer play
                Make_Move.makeComputerMove(Level, humanTurn)
                Draw_Board.drawBoard()
            if(Make_Move.checkForDraw() == 1):
                break
        #check to see who won
        if(Make_Move.checkBoard.checkForWin() == 1):
            print("Computer Wins")
        elif(Make_Move.checkBoard.checkForWin() == -1):
            print("Human Wins")
        else:
            print("The game is a draw")
        Make_Move.resetGame()

    #test the last user condition
    elif (humanTurn == "second" and Level == "hard"):
        while (Make_Move.checkBoard.checkForWin() == 0):
            #make computer move
            Make_Move.makeComputerMove(Level, humanTurn)
            Draw_Board.drawBoard()
            if(Make_Move.checkForDraw() == 1):
                break
            if(Make_Move.checkBoard.checkForWin() == 0):
                #error handling
                validMove = -1
                while (validMove == -1):
                    try:
                        #make human move
                        YourMove = input("What move would you like to make? (1-9)")
                        validMove = Make_Move.playMove(YourMove, "human")
                        Draw_Board.drawBoard()
                    except:
                        print("could not recognize space")
            if(Make_Move.checkForDraw() == 1):
                break
        #figure out who won
        if(Make_Move.checkBoard.checkForWin() == 1):
            print("Computer Wins")
        elif(Make_Move.checkBoard.checkForWin() == -1):
            print("HumanWins")
        else:
            print("The game is a draw")
        Make_Move.resetGame()

#here is where the program run starts
#user enters a loop until they enter a valid answer for the level they want to play
while (1):
    Level = raw_input("What level do you want to play? (easy or hard)")
    if (Level == "easy" or Level == "hard"):
        break
    else:
        print("invalid input, please enter what level you want to play. (easy or hard)")

#user enters another loop until they enter valid input for which order they want to move
while (1):
    MoveFirst = raw_input("Do you want to move first or second? (first or second)")
    if (MoveFirst == "first" or MoveFirst == "second"):
        break
    else:
        print("invalid input, please enter if you want to move first or second. (first or second")

#after successful inputs of the level and order, it's time to play the game!
Play(Level, MoveFirst)

