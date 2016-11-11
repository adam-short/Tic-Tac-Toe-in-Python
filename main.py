#TIC TAC TOE BY FLYNN TESORIERO
#TODO: Get winning working!!

#Default Positions
positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

winner = False



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

#Check if the player wins
#Super hardcore logic found here
def check_win(pos, xo):
    xo_count = pos.count(xo)
    print("\nThere are "+str(xo_count)+" "+xo+"'s")
    if(xo_count > 2):
        #Well let's get started shall we

        #print(xo)

        #3 in a row horizontally (0-2, 3-5, 6-8)
        if(pos[0] == xo and pos[1] == xo and pos[2] == xo):
            return True
        elif(pos[3] == xo and pos[4] == xo and pos[5] == xo):
            return True
        elif (pos[6] == xo and pos[7] == xo and pos[8] == xo):
            return True

        #3 in a row vertically (0,3,6) (1,4,7) (2,5,8)
        if (pos[0] == xo and pos[3] == xo and pos[6] == xo):
            return True
        elif (pos[1] == xo and pos[4] == xo and pos[7] == xo):
            return True
        elif (pos[2] == xo and pos[5] == xo and pos[8] == xo):
            return True

        #3 in a row diagonally (0,4,8) (2,4,6)
        if (pos[0] == xo and pos[4] == xo and pos[8] == xo):
            return True
        elif (pos[2] == xo and pos[4] == xo and pos[6] == xo):
            return True


#For checking the space
#Takes in a position an position number
def check_space(pos, num):
    print(pos[num])
    if(pos[num] != " "):
        print(pos[num])
        print("You fail")
        return False
    else:
        return True

#For choosing a space on the board
#Takes in either an 'x' or an 'o'
def choose(xo):
    print("Choose a space (1-9)")
    space = int(input("Space: "))
    space = space - 1

    if check_space(positions, space):
        positions[space] = xo
        board(positions)

        if check_win(positions, xo):
            print("Winner!!!")
            winner = True
    else:
        return False

#winner variable may be an issue (not global or some shit)
def player_vs_player():
    board(positions)
    i = 1
    while(winner != True):
        print("This is turn number " + str(i))

        if (i % 2 == 0):
            print("\nPlayer 2")
            if choose('o'):
                choose('o')
        else:
            print("\nPlayer 1")
            if choose('x'):
                choose('x')

        i = i + 1

'''
def player_vs_player():
    board(positions)
    print("\nPlayer 1")
    if choose('x'):
        choose('x')

    print("\nPlayer 2")
    if choose('o'):
        choose('o')

    print("\nPlayer 1")
    if choose('x'):
        choose('x')

    print("\nPlayer 2")
    if choose('o'):
        choose('o')

    print("\nPlayer 1")
    if choose('x'):
        choose('x')

    print("\nPlayer 2")
    if choose('o'):
        choose('o')
'''


def player_vs_computer():
    # Difficulty Selection
    print("\nSelect Difficultly")
    print("1: Simple")
    print("2: Hard")

    difficultly_selection = input("Selection: ")
    difficultly_selection = int(difficultly_selection)
    if (difficultly_selection == 1):
        print("Simple")
        difficulty = 1
    elif (difficultly_selection == 2):
        print("Hard")
        difficulty = 2


def play():
    #Player or computer selection
    print("\nSelect Game Mode")
    print("1: Player vs Player")
    print("2: Player vs Computer")

    game_selection = input("Selection: ")
    game_selection = int(game_selection)
    if (game_selection == 1):
        player_vs_player()
    elif (game_selection == 2):
        player_vs_computer()




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
    else:
        menu()


#Menu
def menu():
    print("\nWelcome to Tic Tac Toe in Python!\n")
    print("Select one of the below options:")
    print("1. Play")
    print("2. Help")
    print("3. Quit")

    #Menu selection
    menu_selection = input("Selection: ")
    menu_selection = int(menu_selection)
    if (menu_selection == 1):
        play()
    elif (menu_selection == 2):
        help()
    else:
        print("Bye!")

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