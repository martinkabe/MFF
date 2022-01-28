
class QueensProblem:

    def __init__(self, n):
        self.n = n
        self.chess_table = [[0 for i in range(n)] for j in range(n)]


    def solve_n_queens(self):

        if self.solve(0):
            self.print_queens()
        
        else:
            print("There is no solution to the problem.")
    

    # col_index is the same as the index of the queen
    def solve(self, col_index):
        
        # base case
        if col_index == self.n:
            return True
        
        for row_index in range(self.n):
            if self.is_place_valid(row_index, col_index):
                self.chess_table[row_index][col_index] = 1

                if self.solve(col_index + 1):
                    return True
                
                # BACKTRACK
                print("BACKTRACKING ...")
                self.chess_table[row_index][col_index] = 0
        
        return False

    def is_place_valid(self, row_index, col_index):
        # queens can attack each other horizotally
        for i in range(self.n):
            if self.chess_table[row_index][i] == 1:
                return False
        
        # check the diagonals
        # from top left to bottom right
        j = col_index
        for i in range(row_index, -1, -1):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1
        
        # check the diagonals
        # from top right to bottom left
        j = col_index
        for i in range(row_index, self.n):
            if i < 0:
                break
            if self.chess_table[i][j] == 1:
                return False
            j -= 1

        return True

    def print_queens(self):
        for row in range(self.n):
            for col in range(self.n):
                if self.chess_table[row][col] == 1:
                    print(' Q ', end='')
                else:
                    print(' - ', end='')
            print('\n')


if __name__=="__main__":
    queens = QueensProblem(4)
    queens.solve_n_queens()
    