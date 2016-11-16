#TIC TAC TOE BY FLYNN TESORIERO

#For delays
import time

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

def coltest():
    print(colour.purple+"Purple")
    print(colour.blue+"Blue")
    print(colour.green+"Green")
    print(colour.yellow+"Yellow")
    print(colour.red+"Red\n"+colour.end)


#Set up globals
global winner
global i

#Define globals
winner = False
i = 1

print("===================================\n"+colour.blue+colour.bold+" Welcome to Tic Tac Toe in Python!"+colour.end+"\n===================================\n")

#Colour the X & O's on the board in realtime without changing list
def poscolour(pos, number):
    if(pos[number] == 'x'):
        return colour.green + str(pos[number]) + colour.end
    elif (pos[number] == 'o'):
        return colour.purple + str(pos[number]) + colour.end
    else:
        return pos[number]

#Function to print board
#1 (a) is in the bottom left corner, like a num pad.
#9 (i) in in the top right corner.
def board(pos):
    print(colour.end+"\n┌───┬───┬───┐")
    print("│ "+poscolour(positions,6)+" │ "+poscolour(positions,7)+" │ "+poscolour(positions,8)+" │")
    print("├───┼───┼───┤")
    print("│ "+poscolour(positions,3)+" │ "+poscolour(positions,4)+" │ "+poscolour(positions,5)+" │")
    print("├───┼───┼───┤")
    print("│ "+poscolour(positions,0)+" │ "+poscolour(positions,1)+" │ "+poscolour(positions,2)+" │")
    print("└───┴───┴───┘")

#board(positions)

#Check inputs
#input should be passed as string
def inputcheck(low, high, input):
    try:
        int(input)
    except ValueError:
        return False
    else:
        parsedinput = int(input)
        if(parsedinput <= high and parsedinput >= low):
            return parsedinput
        else:
            return False


#Check if your
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

def win(xo):
    if (xo == "x"):
        print(colour.green + "\n __  __   __        __  ___   _   _   ____  ")
        time.sleep(0.5)
        print(" \ \/ /   \ \      / / |_ _| | \ | | / ___| ")
        time.sleep(0.5)
        print("  \  /     \ \ /\ / /   | |  |  \| | \___ \ ")
        time.sleep(0.5)
        print("  /  \      \ V  V /    | |  | |\  |  ___) |")
        time.sleep(0.5)
        print(" /_/\_\      \_/\_/    |___| |_| \_| |____/ "+colour.end)
        time.sleep(0.5)
    elif (xo == "o"):
        print(colour.purple + "\n   ___     __        __  ___   _   _   ____  ")
        time.sleep(0.5)
        print("  / _ \    \ \      / / |_ _| | \ | | / ___| ")
        time.sleep(0.5)
        print(" | | | |    \ \ /\ / /   | |  |  \| | \___ \ ")
        time.sleep(0.5)
        print(" | |_| |     \ V  V /    | |  | |\  |  ___) |")
        time.sleep(0.5)
        print("  \___/       \_/\_/    |___| |_| \_| |____/ "+colour.end)
        time.sleep(0.5)

#For checking the space
#Takes in a position an position number
def check_space(pos, num):
    #print(pos[num])
    if(pos[num] != " "):
        #print(pos[num])
        print("\nThat spot is taken! Choose a different spot")
        return False
    else:
        return True

#For choosing a space on the board
#Takes in either an 'x' or an 'o'
def choose(xo):
    global winner
    print("Choose a space (1-9)")
    space = int(input("Space: "))
    space = space - 1

    if check_space(positions, space):
        positions[space] = xo
        board(positions)

        if check_win(positions, xo):
            win(xo)
            winner = True
        return True
    else:
        return False


def player_vs_player():
    print(colour.bold+"\n-------------\n Begin Game!\n-------------"+colour.end)
    board(positions)
    global i
    while(winner != True):
        if (i % 2 == 0):
            print(colour.purple+"It's player O's turn!")
            if choose('o'):
                i = i + 1
            #else:
            #    print("choose again")
        else:
            print(colour.green+"It's player X's turn!")
            if choose('x'):
                i = i + 1
            #else:
            #    print("choose again")


def player_vs_computer():
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

    if (inputcheck(1, 2, game_selection) != False):
        game_selection = inputcheck(1, 2, game_selection)
        if (game_selection == 1):
            player_vs_player()
        elif (game_selection == 2):
            player_vs_computer()
    else:
        print(colour.red + "That's not a choice...\n" + colour.end)

def help():
    print(colour.bold+"\n------\n Help\n------"+colour.end)
    print("Tic tac toe is played... bla bla bla")
    print("This is what the board looks like...")
    help_pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    board(help_pos)
    print("\nThe board is numbered from 1 in the bottom left to 9 in the top right, like a computer num pad.")
    print("More description needed...")

    #Take me back...
    if (input("Press enter to return")):
        welcome()
    else:
        welcome()


#Menu
def welcome():
    print(colour.bold+"Select one of the below options:"+colour.end)
    print("1. Play")
    print("2. Help")
    print("3. Quit")

def menu():
    #Menu selection
    menu_selection = input("Selection: ")

    if(inputcheck(1,3,menu_selection) != False):
        menu_selection = inputcheck(1,3,menu_selection)
        # menu_selection = int(menu_selection)
        if (menu_selection == 1):
            play()
        elif (menu_selection == 2):
            help()
        else:
            print(colour.green+"Bye")
            quit()
    else:
        print(colour.red+"That's not a choice...\n"+colour.end)


#Let's get this show on the road!
welcome()

while True:
    menu()

#Unit Tests:
#coltest()
#test = input("test: ")
#inputcheck(1,10,test)

