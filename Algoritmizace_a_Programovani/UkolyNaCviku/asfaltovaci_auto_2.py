import numpy as np

movement = ''

def is_out_parking(n_row, n_col, row_pos, col_pos):
    if (row_pos + 1 > n_row or row_pos < 0) or (col_pos + 1 > n_col or col_pos < 0):
        return(True)
    return(False)


def get_inputs():
    inputs = []
    for i in range(4):
        inputs.append(int(input()))
    return(inputs)


def get_moves():
    inputs = []
    inpt = input()
    while inpt != '0':
        inputs.append(inpt)
        inpt = input()
    return(inputs)


def current_step(move, row_pos, col_pos):
    global movement
    mv = ''
    if move == '-':
        mv = movement
    else:
        mv = move
    if mv == '<':
        return(row_pos, col_pos - 1)
    elif mv == '>':
        return(row_pos, col_pos + 1)
    elif mv == '^':
        return(row_pos - 1, col_pos)
    elif mv == 'v':
        return(row_pos + 1, col_pos)
    else:
        return(row_pos, col_pos)


def create_parking():
    n_cols, n_rows, col_start, row_start = get_inputs()
    if (n_cols < 1 or n_cols > 1e5) or \
        (n_rows < 1 or n_rows > 1e5) or \
        is_out_parking(n_cols, n_rows, col_start, row_start):
        return([], 0, 0)
        
    rows = np.ones((10, 10))
    rows[1:-1, 1:-1] = 0
    rows[row_start+1][col_start+1] = 1
    return([rows, row_start+1, col_start+1])


if __name__ == '__main__':
    parking, row_pos, col_pos = create_parking()
    moves = get_moves()
    if moves[0] != '-' and len(parking) != 0:
        no_steps = 0

        for move in moves:
            if move != '-':
                movement = move
            row_pos, col_pos = current_step(move, row_pos, col_pos)
            no_steps += 1
            if (parking[row_pos][col_pos] != 1):
                parking[row_pos][col_pos] = 1
            else:
                print(f"{no_steps} KO")
                break
            if no_steps == 9:
                print(f"{no_steps} OK")
