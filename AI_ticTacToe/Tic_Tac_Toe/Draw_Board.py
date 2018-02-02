import Make_Move

def drawBoard():
    layout = Make_Move.checkBoard
    SpaceStrings = [" " for i in range(10)]
    for x in range(1,10):
        if (layout.game.Spaces[x].state == 1):
            SpaceStrings[x] = "X"
        elif (layout.game.Spaces[x].state == 10):
            SpaceStrings[x] = "O"

    print("     |     |     ")
    print("  " + SpaceStrings[1] + "  |  " + SpaceStrings[2] + "  |  " + SpaceStrings[3] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + SpaceStrings[4] + "  |  " + SpaceStrings[5] + "  |  " + SpaceStrings[6] + "  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print("  " + SpaceStrings[7] + "  |  " + SpaceStrings[8] + "  |  " + SpaceStrings[9] + "  ")
    print("     |     |     ")
