# -*- coding: utf-8 -*-
import time, random

board = [""]*9
winner = False

class Font:
    purple = "\033[95m"
    blue = "\033[94m"
    green = "\033[92m"
    yellow = "\033[93m"
    red = "\033[91m"
    end = "\033[0m"
    bold = "\033[1m"
    underline = "\033[4m"


print("="*12+"\n")
print(Font.blue + Font.bold)
print("Welcome to Tic Tac Toe in Python!" + Font.end)

#Colour an X or O
def colour(char):
    if(char == 'x'):
        return Font.green + char + Font.end
    elif (char == 'o'):
        return Font.purple + char + Font.end
    else:
        return char

#Function to print board
#1 (a) is in the bottom left corner, like a num pad.
#9 (i) in in the top right corner.
def print_board(pos):
    print(Font.end+"\n┌───┬───┬───┐")
    print("| " + "  | ".join(board[6:9]) + "  |")
    print("├───┼───┼───┤")
    print("| " + "  | ".join(board[3:6]) + "  |")
    print("├───┼───┼───┤")
    print("| " + "  | ".join(board[0:3]) + "  |")
    print("└───┴───┴───┘")

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


def is_all(board_slice, xo):
    return all(xo == tk for tk in board_slice)

#Check if your a winner
def check_win(board, xo):
    #3 in a row horizontally (0,1,2) (3,4,5) (6,7,8)
    if is_all(board[0:3], xo) or is_all(board[3:6], xo) or is_all(board[6:9], xo):
        return True

    #3 in a row vertically (0,3,6) (1,4,7) (2,5,8)
    if is_all(board[0:7:3], xo) or is_all(board[1:8:3] or is_all(board[2:9:3]), xo):
        return True

    #3 in a row diagonally (0,4,8) (2,4,6)
    if is_all(board[0:9:4], xo) or is_all(board[2:7:2]):
        return True

    return False

def check_tie(board):
    return board.count(" ") == 0

def print_win(xo):
    if (xo == "x"):
        print(Font.green + "\n __  __   __        __  ___   _   _   ____  ")
        time.sleep(0.5)
        print(" \ \/ /   \ \      / / |_ _| | \ | | / ___| ")
        time.sleep(0.5)
        print("  \  /     \ \ /\ / /   | |  |  \| | \___ \ ")
        time.sleep(0.5)
        print("  /  \      \ V  V /    | |  | |\  |  ___) |")
        time.sleep(0.5)
        print(" /_/\_\      \_/\_/    |___| |_| \_| |____/ \n"+Font.end)
        time.sleep(0.5)
    elif (xo == "o"):
        print(Font.purple + "\n   ___     __        __  ___   _   _   ____  ")
        time.sleep(0.5)
        print("  / _ \    \ \      / / |_ _| | \ | | / ___| ")
        time.sleep(0.5)
        print(" | | | |    \ \ /\ / /   | |  |  \| | \___ \ ")
        time.sleep(0.5)
        print(" | |_| |     \ V  V /    | |  | |\  |  ___) |")
        time.sleep(0.5)
        print("  \___/       \_/\_/    |___| |_| \_| |____/ \n"+Font.end)
        time.sleep(0.5)

def check_space(board, num):
    return board[num] == " "

def can_choose(xo):
    global board
    print("Choose a space (1-9)")
    space = int(input("Space: ")) - 1

    if check_space(board, space):
        board[space] = xo
        return True
    else:
        return False

def player_vs_player():
    global board
    print(Font.bold+"\n-------------\n Begin Game!\n-------------"+Font.end)
    print_board(board)
    i = 0
    while(winner != True):
        if (i % 2 == 0):
            print(Font.purple+"It's player O's turn!")
            if can_choose('o'):
                i = i + 1
                print_board(board)
            else:
                print("\nThat spot is taken! Choose a different spot")
        else:
            print(Font.green+"It's player X's turn!")
            if can_choose('x'):
                i = i + 1
                print_board(board)
            else:
                print("\nThat spot is taken! Choose a different spot")


def chunk(ls, size):
    size = max(1, size)
    return list((ls[i:i+size] for i in xrange(0, len(ls), size)))

def finishable_by(xo):
    return lambda ls: ls.count(xo) == 2 and ls.count(" ") == 1

def finishing_position(boardSet, xo):
    can_win = finishable_by(xo)
    winnable = next((boardSet.index(n) for n in boardSet if can_win(boardSet)), -1)

    return boardSet[winnable].index(" ") if winnable > -1 else -1

def random_placement():
    rand = random.choice([ind for ind, x in enumerate(board) if x == " "])
    return rand

def ai_placement(board): # returns position to place
    rows = chunk(board, 3)
    cols = [board[0:7:3], board[1:8:3], board[2:9:3]]
    diags = [board[0:9:4], board[2:7:2]]

    win_by_row   = finishing_position(rows, "o")
    win_by_col   = finishing_position(cols, "o")
    win_by_diag  = finishing_position(diags, "o")

    block_row    = finishing_position(rows, "x")
    block_col    = finishing_position(cols, "x")
    block_diag   = finishing_position(diags, "x")

    if win_by_row > -1:
        return win_by_row
    elif win_by_col > -1:
        return win_by_col
    elif win_by_diag > -1:
        return win_by_diag
    elif block_row > -1:
        return block_row
    elif block_col > -1:
        return block_col
    elif block_diag > -1:
        return block_diag
    elif board[4] == " ":
        return 4
    else:
        return random_placement()

def player_vs_computer():
    global board, winner
    print("\nSelect Difficulty.")
    print("1. Simple")
    print("2. Hard")

    difficulty_selection = int(input("Selection: "))
    print(Font.bold + "\n-------------\n Begin Game!\n-------------" + Font.end)
    print_board(board)
    turn = 0

    while (winner != True):
        if (turn % 2 == 0):
            if (difficulty_selection == 1):
                board[random_placement()] = "o"
            else:
                board[ai_placement(board)] = "o"
            turn += 1
        else:
            print(Font.green)
            if can_choose('x'):
                turn += 1
            else:
                print("\nThat spot is taken! Choose a different spot.")

        if check_tie(board):
            print("\nIt's a tie!"+Font.end)
            winner = True
        elif check_win("board", "x"):
            print_win("x")
            winner = True
        elif check_win("board", "o"):
            print_win("o")
            winner = True


    input("Press anything to return to menu.")
    welcome()


def play():
    #Player or computer selection
    print(Font.bold+"\nSelect Game Mode"+Font.end)
    print("1: Player vs Player")
    print("2: Player vs Computer")

    game_selection = int(input("Selection: "))

    if (input_check(1, 2, game_selection) != False):
        game_selection = input_check(1, 2, game_selection)
        if (game_selection == 1):
            player_vs_player()
        elif (game_selection == 2):
            player_vs_computer()
    else:
        print(Font.red + "That's not a choice...\n" + Font.end)

def help():
    print(Font.bold+"\n------\n Help\n------"+Font.end)
    print("Tic tac toe is played by joining 3 X's or O's in a row.")
    help_pos = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print_board(help_pos)
    print("\nThe board is numbered from 1 in the bottom left to 9 in the top right, like a computer num pad.")

    #Take me back...
    input("Press anything to return to menu.")
    welcome()


#Menu
def welcome():
    print(Font.bold+"Select one of the below options:"+Font.end)
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
            print(Font.green+"Bye")
            quit()
    else:
        print(Font.red+"That's not a choice...\n"+Font.end)


#Let's get this show on the road!
welcome()
while True:
    menu()
