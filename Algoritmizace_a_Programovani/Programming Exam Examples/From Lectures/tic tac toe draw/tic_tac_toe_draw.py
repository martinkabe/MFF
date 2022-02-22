import random

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self, r, c):
        for i in range(r):
            row = []
            for j in range(c):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # zkontroluj radky
        cntr = 0
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] == "-":
                    break
                if self.board[i][j] != player:
                    cntr = 0
                    break
                else:
                    cntr += 1
                    break
            
            if win and cntr >= 5:
                if player == 'O':
                    self.board[i][j] = 'X'
                    return True
                else:
                    self.board[i][j] = 'O'
                    return True
            
            if self.board[i][j] == "-":
                break

        return False

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end="")
            print()

    def start(self, rows, columns):
        self.create_board(rows, columns)
        n_rows = len(self.board)
        n_cols = len(self.board[0])
        row = col = 0

        player = 'X' if self.get_random_first_player() == 1 else 'O'

        for row in range(1, n_rows+1):
            for col in range(1, n_cols+1):
                self.fix_spot(row - 1, col - 1, player)

                if self.is_player_win(player):
                    player = self.swap_player_turn(player)

                if self.is_board_filled():
                    break

                player = self.swap_player_turn(player)

        self.show_board()


if __name__=="__main__":
    tic_tac_toe = TicTacToe()
    tic_tac_toe.start(*list(map(int, input().split())))