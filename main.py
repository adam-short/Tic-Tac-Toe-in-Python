#TIC TAC TOE BY FLYNN TESORIERO

#Default Positions
positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

#Function to print board
#1 (a) is in the bottom left corner, like a num pad.
#9 (i) in in the top right corner.
def board(pos):
    print(" _________________")
    print("|     |     |     |")
    print("|  "+pos[6]+"  |  "+pos[7]+"  |  "+pos[8]+"  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  "+pos[3]+"  |  "+pos[4]+"  |  "+pos[5]+"  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  "+pos[0]+"  |  "+pos[1]+"  |  "+pos[2]+"  |")
    print("|_____|_____|_____|")

#board(positions)

def play():
    print("Game here")



def help():
    print("\nHELP")
    print("Tic tac toe is played... bla bla bla")
    print("This is what the board looks like...")
    help_pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    board(help_pos)
    print("\nThe board is numbered from 1 in the bottom left to 9 in the top right, like a computer num pad.")
    print("More description needed...")

    #Back
    if (input("Press enter to return")):
        menu()


#Menu
def menu():
    print("\nWelcome to Tic Tac Toe in Python!\n")
    print("Select one of the below options:")
    print("1. Play")
    print("2. Help")

    #Menu selection
    if(int(input("Selection: ")) == 1):
        play()
    else:
        help()

#run game
menu()


#  _________________
# |     |     |     |
# |  x  |  x  |  x  |
# |_____|_____|_____|
# |     |     |     |
# |  x  |  x  |  x  |
# |_____|_____|_____|
# |     |     |     |
# |  x  |  x  |  x  |
# |_____|_____|_____|