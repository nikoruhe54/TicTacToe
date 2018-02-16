import Make_Move
import Make_4_by_4_Move

def draw4by4Board():
    layout = Make_4_by_4_Move.checkBoard
    SpaceStrings = [" " for i in range(17)]
    for x in range(1,17):
        if (layout.game.Spaces[x].state == 1):
            SpaceStrings[x] = "X"
        elif (layout.game.Spaces[x].state == 10):
            SpaceStrings[x] = "O"
    print("     |     |     |     ")
    print("  " + SpaceStrings[1] + "  |  " + SpaceStrings[2] + "  |  " + SpaceStrings[3] + "  |  " + SpaceStrings[4] + "  ")
    print("_____|_____|_____|_____")
    print("     |     |     |     ")
    print("  " + SpaceStrings[5] + "  |  " + SpaceStrings[6] + "  |  " + SpaceStrings[7] + "  |  " + SpaceStrings[8] + "  ")
    print("_____|_____|_____|_____")
    print("     |     |     |     ")
    print("  " + SpaceStrings[9] + "  |  " + SpaceStrings[10] + "  |  " + SpaceStrings[11] + "  |  " + SpaceStrings[12] + "  ")
    print("_____|_____|_____|_____")
    print("     |     |     |     ")
    print("  " + SpaceStrings[13] + "  |  " + SpaceStrings[14] + "  |  " + SpaceStrings[15] + "  |  " + SpaceStrings[16] + "  ")
    print("     |     |     |     ")

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

