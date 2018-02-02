import Make_Move
import Draw_Board

def Play(level, humanTurn):
    Draw_Board.drawBoard()
    if (humanTurn == "first" and Level == "hard"):
        while (Make_Move.checkBoard.checkForWin() == 0):
            YourMove = input("What move would you like to make? (1-9)")
            Make_Move.playMove(YourMove, "human")
            Draw_Board.drawBoard()
            if(Make_Move.checkBoard.checkForWin() == 0):
                Make_Move.makeComputerMove()
                Draw_Board.drawBoard()
        if(Make_Move.checkBoard.checkForWin() == 1):
            print("Computer Wins")
        else:
            print("Human Wins")
        Make_Move.resetGame()
    elif (humanTurn == "second" and Level == "hard"):
        while (Make_Move.checkBoard.checkForWin() == 0):
            Make_Move.makeComputerMove()
            Draw_Board.drawBoard()
            if(Make_Move.checkBoard.checkForWin() == 0):
                YourMove = input("What move would you like to make? (1-9)")
                Make_Move.playMove(YourMove, "human")
                Draw_Board.drawBoard()
        if(Make_Move.checkBoard.checkForWin() == 1):
            print("Computer Wins")
        else:
            print("HumanWins")
        Make_Move.resetGame()

Level = raw_input("What level do you want to play? (easy or hard)")
MoveFirst = raw_input("Do you want to move first or second? (first or second)")
Play(Level, MoveFirst)

# Draw_Board.drawBoard()
# Make_Move.playMove(5, "human")
# Draw_Board.drawBoard()
# Make_Move.makeComputerMove()
# Draw_Board.drawBoard()
# Make_Move.playMove(8, "human")
# Draw_Board.drawBoard()
# Make_Move.makeComputerMove()
# Draw_Board.drawBoard()
# Make_Move.playMove(7, "human")
# Draw_Board.drawBoard()
# Make_Move.makeComputerMove()
# Draw_Board.drawBoard()
# Make_Move.playMove(6, "human")
# Draw_Board.drawBoard()
# Make_Move.makeComputerMove()
# Draw_Board.drawBoard()
