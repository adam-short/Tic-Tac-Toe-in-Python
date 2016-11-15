#TIC TAC TOE BY FLYNN TESORIERO

#Default Positions
positions = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

#Some nice colour
class colour:
    purple = '\033[95m' #Purple
    blue = '\033[94m' #Dark blue / purple
    green = '\033[92m' #Bright Green
    yellow = '\033[93m' #Yellow
    red = '\033[91m' #red
    end = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

#Set up globals
global winner
global i

#Define globals
winner = False
i = 1

#Function to print board
#1 (a) is in the bottom left corner, like a num pad.
#9 (i) in in the top right corner.
def board(pos):
    print("\n┌───┬───┬───┐")
    print("│ "+pos[6]+" │ "+pos[7]+" │ "+pos[8]+" │")
    print("├───┼───┼───┤")
    print("│ "+pos[3]+" │ "+pos[4]+" │ "+pos[5]+" │")
    print("├───┼───┼───┤")
    print("│ "+pos[0]+" │ "+pos[1]+" │ "+pos[2]+" │")
    print("└───┴───┴───┘")

#board(positions)

#Check if the player wins
def check_win(pos, xo):
    xo_count = pos.count(xo)
    #print("\nThere are "+str(xo_count)+" "+xo+"'s")
    if(xo_count > 2):
        #Below code checks for every possible win, if the amount of player x or o's is above 2

        #3 in a row horizontally (0,1,2) (3,4,5) (6,7,8)
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
    #print(pos[num])
    if(pos[num] != " "):
        #print(pos[num])
        print("That spot is taken!")
        return False
    else:
        return True

#For choosing a space on the board
#Takes in either an 'x' or an 'o'
def choose(xo):
    global winner
    print("-------")
    print("Choose a space (1-9)")
    space = int(input("Space: "))
    space = space - 1

    if check_space(positions, space):
        positions[space] = xo
        board(positions)

        if check_win(positions, xo):
            print("Winner!!!")
            winner = True
        return True
    else:
        return False

#winner variable may be an issue (not global or some shit)
def player_vs_player():
    print("\n-------------\n Begin Game!\n-------------")
    board(positions)
    global i
    while(winner != True):
        if (i % 2 == 0):
            print("Player O")
            if choose('o'):
                i = i + 1
            else:
                print("choose again")
        else:
            print("Player X")
            if choose('x'):
                i = i + 1
            else:
                print("choose again")


    #Ran once the game has been run
    print("End")


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
    print(colour.bold+"\nSelect Game Mode"+colour.end)
    print("1: Player vs Player")
    print("2: Player vs Computer")

    game_selection = input("Selection: ")
    game_selection = int(game_selection)
    if (game_selection == 1):
        player_vs_player()
    elif (game_selection == 2):
        player_vs_computer()




def help():
    print("\n------\n Help\n------")
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
    print("===================================\n"+colour.green+" Welcome to Tic Tac Toe in Python!"+colour.end+"\n===================================\n")
    print(colour.bold+"Select one of the below options:"+colour.end)
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

#Let's get this show on the road!
menu()