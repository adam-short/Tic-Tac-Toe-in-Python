#TIC TAC TOE BY FLYNN TESORIERO
#TODO: Clean the positions list after winning

#For delays
import time

#For computer player
import random

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
def input_check(low, high, input):
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


#Check if your a winner
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

def check_tie(pos):
    for i in pos:
        if(i == " "):
            return False
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
        print(" /_/\_\      \_/\_/    |___| |_| \_| |____/ \n"+colour.end)
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
        print("  \___/       \_/\_/    |___| |_| \_| |____/ \n"+colour.end)
        time.sleep(0.5)

#For checking the space
#Takes in a position an position number
def check_space(pos, num):
    #print(pos[num])
    if(pos[num] != " "):
        #print(pos[num])
        #print("\nThat spot is taken! Choose a different spot")
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
        #board(positions)

        if check_win(positions, xo):
            win(xo)
            winner = True
        elif check_tie(positions):
            print("\nIt's a tie!"+colour.end)
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
                board(positions)
            else:
                print("\nThat spot is taken! Choose a different spot")
        else:
            print(colour.green+"It's player X's turn!")
            if choose('x'):
                i = i + 1
                board(positions)
            else:
                print("\nThat spot is taken! Choose a different spot")



def check1(positions, xo):
    if (positions[6] == xo and positions[8] == xo):
        if positions[7] == " ":
            positions[7] = 'x'
            return True
        else:
            return False
    elif (positions[0] == xo and positions[6] == xo):
        if positions[3] == " ":
            positions[3] = 'x'
            return True
        else:
            return False
    elif (positions[1] == xo and positions[7] == xo):
        if positions[4] == " ":
            positions[4] = 'x'
            return True
        else:
            return False
    elif (positions[2] == xo and positions[8] == xo):
        if positions[5] == " ":
            positions[5] = 'x'
            return True
        else:
            return False
    elif (positions[6] == xo and positions[8] == xo):
        if positions[7] == " ":
            positions[7] = 'x'
            return True
        else:
            return False
    elif (positions[3] == xo and positions[5] == xo):
        if positions[4] == " ":
            positions[4] = 'x'
            return True
        else:
            return False
    elif (positions[0] == xo and positions[2] == xo):
        if positions[1] == " ":
            positions[1] = 'x'
            return True
        else:
            return False
    elif (positions[0] == xo and positions[8] == xo):
        if positions[4] == " ":
            positions[4] = 'x'
            return True
        else:
            return False
    elif (positions[6] == xo and positions[2] == xo):
        if positions[4] == " ":
            positions[4] = 'x'
            return True
        else:
            return False
    # Horo
    # First row
    elif (positions[0] == xo and positions[1] == xo):
        if positions[2] == " ":
            positions[2] = 'x'
            return True
        else:
            return False
    elif (positions[1] == xo and positions[2] == xo):
        if positions[0] == " ":
            positions[0] = 'x'
            return True
        else:
            return False
    # Second row
    elif (positions[3] == xo and positions[4] == xo):
        if positions[5] == " ":
            positions[5] = 'x'
            return True
        else:
            return False
    elif (positions[4] == xo and positions[5] == xo):
        if positions[3] == " ":
            positions[3] = 'x'
            return True
        else:
            return False
    # Third Row
    elif (positions[6] == xo and positions[7] == xo):
        if positions[8] == " ":
            positions[8] = 'x'
            return True
        else:
            return False
    elif (positions[7] == xo and positions[8] == xo):
        if positions[6] == " ":
            positions[6] = 'x'
            return True
        else:
            return False

    # Vertical
    # First
    elif (positions[0] == xo and positions[3] == xo):
        positions[6] = 'x'
        if positions[6] == " ":
            positions[6] = 'x'
            return True
        else:
            return False
    elif (positions[1] == xo and positions[4] == xo):
        if positions[7] == " ":
            positions[7] = 'x'
            return True
        else:
            return False
    elif (positions[2] == xo and positions[5] == xo):
        if positions[8] == " ":
            positions[8] = 'x'
            return True
        else:
            return False
    # Second
    elif (positions[3] == xo and positions[6] == xo):
        if positions[0] == " ":
            positions[0] = 'x'
            return True
        else:
            return False
    elif (positions[4] == xo and positions[7] == xo):
        if positions[1] == " ":
            positions[1] = 'x'
            return True
        else:
            return False
    elif (positions[5] == xo and positions[8] == xo):
        if positions[2] == " ":
            positions[2] = 'x'
            return True
        else:
            return False

    # Diag
    elif (positions[0] == xo and positions[4] == xo):
        if positions[8] == " ":
            positions[8] = 'x'
            return True
        else:
            return False
    elif (positions[4] == xo and positions[8] == xo):
        if positions[0] == " ":
            positions[0] = 'x'
            return True
        else:
            return False
    elif (positions[2] == xo and positions[4] == xo):
        if positions[2] == " ":
            positions[2] = 'x'
            return True
        else:
            return False
    elif (positions[4] == xo and positions[6] == xo):
        if positions[2] == " ":
            positions[2] = 'x'
            return True
        else:
            return False

    else:
        return False


def computer_easy():
    global winner
    rand = randint(0,8)
    #print(rand)
    if check_space(positions, rand):
        positions[rand] = 'o'
        if check_win(positions, 'o'):
            win('o')
            winner = True
        elif check_tie(positions):
            print("\nIt's a tie!"+colour.end)
            winner = True
        #board(positions)
        return True


def computer_hard(turn):
    global winner
    print(turn)
    if(turn == 1):
        print("Computer 1")
        positions[6] = 'x'
        return True

    if (turn == 3):
        print("Computer 2")
        if check_space(positions, 2):
            positions[2] = 'x'
        else:
            positions[0] = 'x'
        return True

    if (turn == 5):
        print(colour.end+"Computer 3")
        if check1(positions, 'x'):
            if check_win(positions, 'x'):
                win('x')
                winner = True
        elif check1(positions, 'o'):
            if check_win(positions, 'x'):
                win('x')
                winner = True
        else:
            if check_space(positions, 6):
                positions[6] = 'x'
            elif check_space(positions, 8):
                positions[8] = 'x'
            elif check_space(positions, 0):
                positions[0] = 'x'
            elif check_space(positions, 2):
                positions[2] = 'x'
        return True

    if (turn == 7):
        print(colour.end+"Computer 4")
        if check1(positions, 'x'):
            print("y")
            if check_win(positions, 'x'):
                win('x')
                winner = True
        elif check1(positions, 'o'):
            print("ye")
            if check_win(positions, 'x'):
                win('x')
                winner = True
        else:
            print("yes")
            if check_space(positions, 6):
                positions[6] = 'x'
            elif check_space(positions, 8):
                positions[8] = 'x'
            elif check_space(positions, 0):
                positions[0] = 'x'
            elif check_space(positions, 2):
                positions[2] = 'x'
        return True

    if (turn == 9):
        print(colour.end+"Computer 5")
        if check_space(positions, 0):
            positions[0] = 'x'
        elif check_space(positions, 1):
            positions[1] = 'x'
        elif check_space(positions, 2):
            positions[2] = 'x'
        elif check_space(positions, 3):
            positions[3] = 'x'
        elif check_space(positions, 4):
            positions[4] = 'x'
        elif check_space(positions, 5):
            positions[5] = 'x'
        elif check_space(positions, 6):
            positions[6] = 'x'
        elif check_space(positions, 7):
            positions[7] = 'x'
        elif check_space(positions, 8):
            positions[8] = 'x'
        return True


def player_vs_computer():
    print("\nSelect Difficultly")
    print("1: Simple")
    print("2: Hard")

    difficultly_selection = input("Selection: ")
    difficultly_selection = int(difficultly_selection)

    if (difficultly_selection == 1):
        print(colour.bold + "\n-------------\n Begin Game!\n-------------" + colour.end)
        board(positions)
        global i
        while (winner != True):
            if (i % 2 == 0):
                #print(colour.purple + "It's the computers turn!"+colour.end)
                if computer_easy():
                    board(positions)
                    i = i + 1
                #else:
                #    print("\nThat spot is taken! Choose a different spot")
            else:
                print(colour.green)
                if choose('x'):
                    i = i + 1
                    #board(positions)
                else:
                    print("\nThat spot is taken! Choose a different spot")

        # Take me back...
        if (input("Press enter to return to menu")):
            print("\n")
            welcome()
        else:
            print("\n")
            welcome()


    elif (difficultly_selection == 2):
        print("Hard")
        print(colour.bold + "\n-------------\n Begin Game!\n-------------" + colour.end)
        board(positions)
        global y
        y = 1
        while (winner != True):
            if (y % 2 == 0):
                print(colour.green)
                if choose('o'):
                    y = y + 1
                    # board(positions)
                else:
                    print("\nThat spot is taken! Choose a different spot")
            else:
                # print(colour.purple + "It's the computers turn!"+colour.end)
                if computer_hard(y):
                    board(positions)
                    y = y + 1
                    # else:
                    #    print("\nThat spot is taken! Choose a different spot")

def play():
    #Player or computer selection
    print(colour.bold+"\nSelect Game Mode"+colour.end)
    print("1: Player vs Player")
    print("2: Player vs Computer")

    game_selection = input("Selection: ")

    game_selection = int(game_selection)

    if (input_check(1, 2, game_selection) != False):
        game_selection = input_check(1, 2, game_selection)
        if (game_selection == 1):
            player_vs_player()
        elif (game_selection == 2):
            player_vs_computer()
    else:
        print(colour.red + "That's not a choice...\n" + colour.end)

def help():
    print(colour.bold+"\n------\n Help\n------"+colour.end)
    print("Tic tac toe is played by joining 3 X's or O's in a row.")
    help_pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    board(help_pos)
    print("\nThe board is numbered from 1 in the bottom left to 9 in the top right, like a computer num pad.")
    #print("More description needed...")

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

    if(input_check(1,3,menu_selection) != False):
        menu_selection = input_check(1,3,menu_selection)
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
#input_check(1,10,test)