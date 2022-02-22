from collections import deque

def print_maze(maze):
    print()
    for row in range(len(maze)):
        print(*maze[row], sep=" ")
    print()

def read_data():
    maze = []
    for i in range(8) :
        maze.append( ["."] * 8 )

    no_obstacles = int(input())
    # obstacles = []
    for i in range(no_obstacles):
        obstacle = list(map(int, input().split()))
        obstacle[0] = obstacle[0] - 1
        obstacle[1] = obstacle[1] - 1
        maze[obstacle[0]][obstacle[1]] = "#"
        # obstacles.append(tuple(obstacle))

    start = list(map(int, input().split()))
    start[0] = start[0] - 1
    start[1] = start[1] -1
    maze[start[0]][start[1]] = "S"

    target = list(map(int, input().split()))
    target[0] = target[0] - 1
    target[1] = target[1] - 1
    maze[target[0]][target[1]] = "E"

    return maze, start, target

def solveMaze(maze, start, target):
    R, C = len(maze), len(maze[0])

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
    visited = [[False] * C for _ in range(R)]

    ### BFS Algo
    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        # if we reached the target
        if coord[0] == target[0] and coord[1] == target[1]:
            return coord[2]

        for dir in directions:
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if (nr < 0 or nr >= R or nc < 0 or nc >= C or maze[nr][nc] == "#" or visited[nr][nc]): continue
            queue.appendleft((nr, nc, coord[2]+1))
    
    return -1


maze, start, target = read_data()
# print_maze(maze)
result = solveMaze(maze, start, target)
print(result)


### TEST CASES

# 1
# 2 1
# 1 1
# 2 2

# 4
# 1 2
# 3 2
# 3 3
# 3 4
# 1 1
# 8 8

# 11
# 1 2
# 3 1
# 3 2
# 3 3
# 3 4
# 7 8
# 7 7
# 7 6
# 7 5
# 7 4
# 7 3
# 1 1
# 8 8

# 8
# 2 1
# 2 2
# 2 3
# 2 4
# 2 5
# 2 6
# 2 7
# 2 8
# 1 1
# 8 8