from collections import deque

maze = []

def print_maze():
    global maze
    print()
    for row in range(len(maze)):
        print(*maze[row], sep=" ")
    print()

def read_data():
    global maze
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

    return start, target

def is_move_possible(coord, dir):
    global maze
    R, C = len(maze), len(maze[0])
    old_c, old_r = coord[0], coord[1]
    new_c, new_r = old_c+dir[0], old_r+dir[1]

    if old_r < 0 or new_r < 0 or old_r >= R or new_r >= R or \
        new_c < 0 or old_c < 0 or new_c >= C or old_c >= C:
        return False

    c1 = r1 = 0
    if abs(dir[0]) > abs(dir[1]): # move in cols direction first
        if dir[0] < 0: # to the left
            for c in range(-1, dir[0]-1, -1):
                c1 = old_c+c
                r1 = old_r
                if maze[c1][r1] == "#": return False
            if maze[c1][r1+dir[1]] == "#": return False
        else: # to the right
            for c in range(1, dir[0]+1):
                c1 = old_c+c
                r1 = old_r
                if maze[c1][r1] == "#": return False
            if maze[c1][r1+dir[1]] == "#": return False
    else: # move in rows direction first
        if dir[1] > 0: # move up first
            for r in range(1, dir[1]+1):
                c1 = old_c
                r1 = old_r + r
                if maze[c1][r1] == "#": return False
            if maze[c1+dir[0]][r1] == "#": return False
        else: # move down first
            for r in range(-1, dir[1]-1, -1):
                c1 = old_c
                r1 = old_r + r
                if maze[c1][r1] == "#": return False
            if maze[c1+dir[0]][r1] == "#": return False

    return True

def solveMaze(start, target):
    global maze
    R, C = len(maze), len(maze[0])

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    
    directions = [
        (-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]

    visited = [[False] * C for _ in range(R)]

    ### BFS Algo
    while len(queue) != 0:
        coord = queue.pop()
        visited[coord[0]][coord[1]] = True

        # if we reached the target
        if coord[0] == target[0] and coord[1] == target[1]:
            return coord[2]

        for dir in directions:
            # print(dir)
            nr, nc = coord[0]+dir[0], coord[1]+dir[1]
            if not is_move_possible(coord, dir) or visited[nr][nc]: continue
            queue.appendleft((nr, nc, coord[2]+1))
    
    return -1


start, target = read_data()
print_maze()
result = solveMaze(start, target)
print(result)


### TEST CASES

# 0
# 1 2
# 8 8

# 3
# 2 1
# 2 2
# 2 3
# 1 1
# 8 8

# 3
# 1 2
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

# 12
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
# 7 2
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