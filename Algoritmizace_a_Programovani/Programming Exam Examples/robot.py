import re


def main():
    # get path of robot using command line by user
    var = input("Please enter path of robot: ")
    # convert input value to upper case
    var = var.upper()
    # check whether input value is valid or not
    var = checkInputValue(var)
    # print the path of robot in console prompt
    printRobotPath(var)


# this function is for check whether input value is valid or not
def checkInputValue(var):
    var = re.sub('[^FLRUD<>]', '', var)
    var = var.split(".")[0]
    return var


# this function is for find current direction, pose of robot
def findDirection(current_direction, current_sight, current_pose, var):
    if current_direction == 0:
        if current_pose == 0:
            if current_sight == 1:
                if var == "L":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
        elif current_pose == 1:
            if current_sight == 1:
                if var == "L":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
        elif current_pose == 2:
            if current_sight == 1:
                if var == "L":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
        elif current_pose == 3:
            if current_sight == 1:
                if var == "L":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose

    elif current_direction == 1:
        if current_pose == 0:
            if current_sight == 1:
                if var == "L":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
        elif current_pose == 1:
            if current_sight == 1:
                if var == "L":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
        elif current_pose == 2:
            if current_sight == 1:
                if var == "L":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose

        elif current_pose == 3:
            if current_sight == 1:
                if var == "L":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
    elif current_direction == 2:
        if current_pose == 0:
            if current_sight == 1:
                if var == "L":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
        elif current_pose == 1:
            if current_sight == 1:
                if var == "L":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
        elif current_pose == 2:
            if current_sight == 1:
                if var == "L":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 0
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 3
                    return current_direction, current_sight, current_pose

        elif current_pose == 3:
            if current_sight == 1:
                if var == "L":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 2
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
            else:
                if var == "L":
                    current_direction = 1
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "R":
                    current_direction = 1
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "U":
                    current_direction = 0
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == "D":
                    current_direction = 0
                    current_sight = 1
                    current_pose = 2
                    return current_direction, current_sight, current_pose
                elif var == "<":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 1
                    return current_direction, current_sight, current_pose
                elif var == ">":
                    current_direction = 2
                    current_sight = -1
                    current_pose = 2
                    return current_direction, current_sight, current_pose


# this function is for print the path of robot according to command by user
def printRobotPath(var):
    current_sight = 1
    current_direction = 2
    current_pose = 2
    initial_path = [0, 0, 0]
    for com in var:
        if com == "F":
            initial_path[current_direction] = initial_path[current_direction] + current_sight
            path = initial_path
            print(str(" ".join(str(x) for x in path)))
        else:
            current_direction, current_sight, current_pose = findDirection(current_direction, current_sight,
                                                                           current_pose, com)
            print(str(" ".join(str(x) for x in initial_path)))


if __name__ == "__main__":
    main()
