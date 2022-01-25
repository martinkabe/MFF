movement = ''

def is_out_parking(n_row, n_col, row_pos, col_pos):
    if (row_pos >= n_row or row_pos < 0) or (col_pos >= n_col or col_pos < 0):
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
        return(None, None)


def parking_info():
    n_cols, n_rows, col_start, row_start = get_inputs()
    if (n_cols < 1 or n_cols > 1e5) or \
        (n_rows < 1 or n_rows > 1e5) or \
        is_out_parking(n_cols, n_rows, col_start, row_start):
        return(0, 0, 0, 0)
    return(n_cols, n_rows, col_start, row_start)


if __name__ == '__main__':
    col_bound, row_bound, col_pos, row_pos = parking_info()
    parking = {}
    parking[(row_pos, col_pos)] = True
    no_steps = 0
    statement = "OK"
    move = input()
    if col_bound != 0 and row_bound != 0:
        while move != "0":
            if move == '-' and no_steps == 0:
                continue
            if move != '-':
                movement = move
            row_pos, col_pos = current_step(move, row_pos, col_pos)
            if row_pos is not None and col_pos is not None:
                no_steps += 1
                if not is_out_parking(row_bound, col_bound, row_pos, col_pos):
                    if (row_pos, col_pos) in parking:
                        statement = "KO"
                        break
                    else:
                        parking[(row_pos, col_pos)] = True
                else:
                    statement = "KO"
                    break
            move = input()
        
        print(f"{no_steps} {statement}")