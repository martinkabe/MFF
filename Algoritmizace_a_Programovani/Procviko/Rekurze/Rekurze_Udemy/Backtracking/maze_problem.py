from collections import deque

class MazeProblem:

    def __init__(self, maze):
        self.maze = maze
        self.x_moves = [1, 0, -1, 0]
        self.y_moves = [0, 1, 0, -1]
        self.n = len(self.maze)
        self.maze_visited = [[False for _ in range(self.n)] for _ in range(self.n)]
    
    def solve_problem(self, start, target, distance):
        queue = deque()
        queue.append((start[0], start[1], distance))

        # BFS algo
        while len(queue) > 0:
            step = queue.pop()
            self.maze_visited[step[0]][step[1]] = True

            if step[0] == target[0] and step[1] == target[1]:
                return step[2]
            
            for direction in range(len(self.x_moves)):
                new_x_move = step[0] + self.x_moves[direction]
                new_y_move = step[1] + self.y_moves[direction]

                if self.is_valid_move(new_x_move, new_y_move):
                    queue.appendleft((new_x_move, new_y_move, step[2] + 1))
        
        return -1
        
    def is_valid_move(self, x, y):
        if x < 0 or x >= self.n:
            return False
        
        if y < 0 or y >= self.n:
            return False

        # if already visited or there is a obstacle
        if self.maze_visited[x][y] == True or self.maze[x][y] == 0:
            return False
        
        return True


if __name__ == '__main__':

    m = [[1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1]]
    
    maze_problem = MazeProblem(m)
    result = maze_problem.solve_problem((0, 0), (4,4), 0)
    if result != -1:
        print(f"Minimum number of steps is {result}.")
    else:
        print("No solution for this maze!")