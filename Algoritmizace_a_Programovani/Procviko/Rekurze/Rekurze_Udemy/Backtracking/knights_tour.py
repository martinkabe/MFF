class KnightsTour:

    def __init__(self, board_size):
        self.board_size = board_size
        # possible horizontal components of the moves
        self.x_moves = [2, 1, -1, -2, -2, -1, 1, 2]
        self.y_moves = [1, 2, 2, 1, -1, -2, -2, -1]
        self.solution_matrix = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.backtracking_steps = 0

    def solve_problem(self):

        # we start with the top left cell
        self.solution_matrix[0][0] = 0
        
        # first parameter is the counter
        # second and the third parameter is the location (0, 0)
        if self.solve(1, 0, 0):
            self.print_solution()
            print(f"#Backtracking steps = {self.backtracking_steps}")
        else:
            print("There is no feasible solution to the problem")
        
    def solve(self, step_counter, x, y):

        # BASE CASE
        if step_counter == self.board_size**2:
            return True
        
        # we have to consider all the possible moves and find the valid one
        for move_index in range(len(self.y_moves)):
            
            next_x = x + self.x_moves[move_index]
            next_y = y + self.y_moves[move_index]

            if self.is_valid_move(next_x, next_y):
                # it is valid step so we can update the solution matrix
                self.solution_matrix[next_x][next_y] = step_counter

                if self.solve(step_counter + 1, next_x, next_y):
                    return True
                
                # BACKTRACKING
                # reinitialize the solution matrix with -1
                self.solution_matrix[next_x][next_y] = -1
                self.backtracking_steps += 1

        return False
    
    def is_valid_move(self, x, y):

        # knight will not step outside the chessboard
        # knight leaves the board horizotally
        if x < 0 or x >= self.board_size:
            return False
        
        # knight leaves the board vertically
        if y < 0 or y >= self.board_size:
            return False
        
        # already visited cell on the chessboard
        if self.solution_matrix[x][y] > -1:
            return False
        
        # valid step
        return True

    def print_solution(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                print(self.solution_matrix[i][j], end=' ')
            print('\n')


if __name__ == '__main__':
    tour = KnightsTour(6)
    tour.solve_problem()