def worker(positions):
    # Horo
    # First row
    if (positions[0] == 'x' and positions[1] == 'x'):
        if positions[2] == " ":
            positions[2] = 'o'
            return True
        else:
            return False
    elif (positions[1] == 'x' and positions[2] == 'x'):
        if positions[0] == " ":
            positions[0] = 'o'
            return True
        else:
            return False
    # Second row
    elif (positions[3] == 'x' and positions[4] == 'x'):
        if positions[5] == " ":
            positions[5] = 'o'
            return True
        else:
            return False
    elif (positions[4] == 'x' and positions[5] == 'x'):
        if positions[3] == " ":
            positions[3] = 'o'
            return True
        else:
            return False
    # Third Row
    elif (positions[6] == 'x' and positions[7] == 'x'):
        if positions[8] == " ":
            positions[8] = 'o'
            return True
        else:
            return False
    elif (positions[7] == 'x' and positions[8] == 'x'):
        if positions[6] == " ":
            positions[6] = 'o'
            return True
        else:
            return False

    # Vertical
    # First
    elif (positions[0] == 'x' and positions[3] == 'x'):
        positions[6] = 'o'
        if positions[6] == " ":
            positions[6] = 'o'
            return True
        else:
            return False
    elif (positions[1] == 'x' and positions[4] == 'x'):
        if positions[7] == " ":
            positions[7] = 'o'
            return True
        else:
            return False
    elif (positions[2] == 'x' and positions[5] == 'x'):
        if positions[8] == " ":
            positions[8] = 'o'
            return True
        else:
            return False
    # Second
    elif (positions[3] == 'x' and positions[6] == 'x'):
        if positions[0] == " ":
            positions[0] = 'o'
            return True
        else:
            return False
    elif (positions[4] == 'x' and positions[7] == 'x'):
        if positions[1] == " ":
            positions[1] = 'o'
            return True
        else:
            return False
    elif (positions[5] == 'x' and positions[8] == 'x'):
        if positions[2] == " ":
            positions[2] = 'o'
            return True
        else:
            return False

    # Diag
    elif (positions[0] == 'x' and positions[4] == 'x'):
        if positions[8] == " ":
            positions[8] = 'o'
            return True
        else:
            return False
    elif (positions[4] == 'x' and positions[8] == 'x'):
        if positions[0] == " ":
            positions[0] = 'o'
            return True
        else:
            return False
    elif (positions[2] == 'x' and positions[4] == 'x'):
        if positions[2] == " ":
            positions[2] = 'o'
            return True
        else:
            return False
    elif (positions[4] == 'x' and positions[6] == 'x'):
        if positions[2] == " ":
            positions[2] = 'o'
            return True
        else:
            return False

    else:
        return False

def worker1(positions):
    # Horo
    # First row
    if (positions[0] == 'o' and positions[1] == 'o'):
        if positions[2] == " ":
            positions[2] = 'o'
            return True
        else:
            return False
    elif (positions[1] == 'o' and positions[2] == 'o'):
        if positions[0] == " ":
            positions[0] = 'o'
            return True
        else:
            return False
    # Second row
    elif (positions[3] == 'o' and positions[4] == 'o'):
        if positions[5] == " ":
            positions[5] = 'o'
            return True
        else:
            return False
    elif (positions[4] == 'o' and positions[5] == 'o'):
        if positions[3] == " ":
            positions[3] = 'o'
            return True
        else:
            return False
    # Third Row
    elif (positions[6] == 'o' and positions[7] == 'o'):
        if positions[8] == " ":
            positions[8] = 'o'
            return True
        else:
            return False
    elif (positions[7] == 'o' and positions[8] == 'o'):
        if positions[6] == " ":
            positions[6] = 'o'
            return True
        else:
            return False

    # Vertical
    # First
    elif (positions[0] == 'o' and positions[3] == 'o'):
        positions[6] = 'o'
        if positions[6] == " ":
            positions[6] = 'o'
            return True
        else:
            return False
    elif (positions[1] == 'o' and positions[4] == 'o'):
        if positions[7] == " ":
            positions[7] = 'o'
            return True
        else:
            return False
    elif (positions[2] == 'o' and positions[5] == 'o'):
        if positions[8] == " ":
            positions[8] = 'o'
            return True
        else:
            return False
    # Second
    elif (positions[3] == 'o' and positions[6] == 'o'):
        if positions[0] == " ":
            positions[0] = 'o'
            return True
        else:
            return False
    elif (positions[4] == 'o' and positions[7] == 'o'):
        if positions[1] == " ":
            positions[1] = 'o'
            return True
        else:
            return False
    elif (positions[5] == 'o' and positions[8] == 'o'):
        if positions[2] == " ":
            positions[2] = 'o'
            return True
        else:
            return False

    # Diag
    elif (positions[0] == 'o' and positions[4] == 'o'):
        if positions[8] == " ":
            positions[8] = 'o'
            return True
        else:
            return False
    elif (positions[4] == 'o' and positions[8] == 'o'):
        if positions[0] == " ":
            positions[0] = 'o'
            return True
        else:
            return False
    elif (positions[2] == 'o' and positions[4] == 'o'):
        if positions[6] == " ":
            positions[6] = 'o'
            return True
        else:
            return False
    elif (positions[4] == 'o' and positions[6] == 'o'):
        if positions[2] == " ":
            positions[2] = 'o'
            return True
        else:
            return False
    else:
        return False