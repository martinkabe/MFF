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

def is_move_possible(coord, new_r, new_c):
    global maze
    R, C = len(maze), len(maze[0])
    old_r, old_c = coord[0], coord[1]

    if old_r < 0 or new_r < 0 or old_r >= R or new_r >= R or new_c < 0 or old_c < 0 or new_c >= C or old_c >= C:
        return False

    # column movement
    if old_r == new_r:
        diff = abs(old_c - new_c)
        for i in range(1, diff+1):
            if old_c < new_c: # move right
                if maze[new_r][old_c+i] == "#":
                    return False
            else: # move left
                if maze[new_r][old_c-i] == "#":
                    return False
    # row movement
    elif old_c == new_c:
        diff = abs(old_r - new_r)
        for i in range(1, diff+1):
            if old_r < new_r: # move down
                if maze[old_r+i][new_c] == "#":
                    return False
            else: # move up
                if maze[old_r-i][new_c] == "#":
                    return False
    # first quadrant diagonal
    elif old_r > new_r and old_c < new_c:
        diff = abs(new_r - old_r)
        for i in range(1, diff+1):
            if maze[old_r-i][old_c+i] == "#":
                return False
    # second quadrant diagonal
    elif old_r > new_r and old_c > new_c:
        diff = abs(new_r - old_r)
        for i in range(1, diff+1):
            if maze[old_r-i][old_c-i] == "#":
                return False
    # third quadrant diagonal
    elif old_r < new_r and old_c > new_c:
        diff = abs(new_r - old_r)
        for i in range(1, diff+1):
            if maze[old_r+i][old_c-i] == "#":
                return False
    # fourth quadrant diagonal
    elif old_r < new_r and old_c < new_c:
        diff = abs(new_r - old_r)
        for i in range(1, diff+1):
            if maze[old_r+i][old_c+i] == "#":
                return False
        
    return True

def solveMaze(start, target):
    global maze
    R, C = len(maze), len(maze[0])

    queue = deque()
    queue.appendleft((start[0], start[1], 0))
    # directions = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)] # king
    # directions = [
    #     (1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1),
    #     (2,0),(-2,0),(0,2),(0,-2),(2,2),(-2,2),(2,-2),(-2,-2),
    #     (3,0),(-3,0),(0,3),(0,-3),(3,3),(-3,3),(3,-3),(-3,-3),
    #     (4,0),(-4,0),(0,4),(0,-4),(4,4),(-4,4),(4,-4),(-4,-4),
    #     (5,0),(-5,0),(0,5),(0,-5),(5,5),(-5,5),(5,-5),(-5,-5),
    #     (6,0),(-6,0),(0,6),(0,-6),(6,6),(-6,6),(6,-6),(-6,-6),
    #     (7,0),(-7,0),(0,7),(0,-7),(7,7),(-7,7),(7,-7),(-7,-7)
    # ] # queen
    directions = [
        (1,0),(-1,0),(0,1),(0,-1),
        (2,0),(-2,0),(0,2),(0,-2),
        (3,0),(-3,0),(0,3),(0,-3),
        (4,0),(-4,0),(0,4),(0,-4),
        (5,0),(-5,0),(0,5),(0,-5),
        (6,0),(-6,0),(0,6),(0,-6),
        (7,0),(-7,0),(0,7),(0,-7)
    ] # rook

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
            if not is_move_possible(coord, nr, nc) or visited[nr][nc]: continue
            queue.appendleft((nr, nc, coord[2]+1))
    
    return -1


start, target = read_data()
print_maze()
result = solveMaze(start, target)
print(result)


### TEST CASES

# 3
# 2 1
# 2 2
# 2 3
# 1 1
# 8 8

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