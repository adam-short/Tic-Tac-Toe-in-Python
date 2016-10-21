places = [False, False, False, False, False, False, False, False, False]

for i in places:
    print(i)

#Function to print board
#1 (a) is in the bottom left corner, like a numpad.
#9 (i) in in the top right corner.
def board(a, b, c, d, e, f, g, h, i):
    print(" _________________")
    print("|     |     |     |")
    print("|  "+g+"  |  "+h+"  |  "+i+"  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  "+d+"  |  "+e+"  |  "+f+"  |")
    print("|_____|_____|_____|")
    print("|     |     |     |")
    print("|  "+a+"  |  "+b+"  |  "+c+"  |")
    print("|_____|_____|_____|")

board("x", " ", "o", "x", "x", "x", "x", "x", "o")

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