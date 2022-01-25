from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.x = data
        self.left = left
        self.right = right


def print_nodes_recursion(root):
    if root is None:
        return
    
    print(root.x, end=" ") # pre-order
    print_nodes_recursion(root.left)
    print_nodes_recursion(root.right)
    
# DFS
def print_nodes_iter_dfs(root):
    l = []
    l.append(root)
    while l:
        node = l.pop()
        if node != None:
            print(node.x, end=" ")
            l.append(node.left)
            l.append(node.right)

# BFS
def print_nodes_iter_bfs(root):
    q = deque()
    q.appendleft(root)
    while q:
        node = q.popleft()
        if node != None:
            print(node.x, end=" ")
            q.appendleft(node.left)
            q.appendleft(node.right)

# Compute height of the tree
def height(root):
    if root is None:
        return 0
    
    left_ans = height(root.left)
    right_ans = height(root.right)

    return max(left_ans, right_ans) + 1

# average height of the tree
paths_list = []
def pathsRec(root, path=[], pathLen=0):
    # Base condition - if binary tree is
    # empty return
    if root is None:
        return

    # add current root's data into 
    # path_ar list
    
    # if length of list is gre
    if(len(path) > pathLen): 
        path[pathLen] = root.x
    else:
        path.append(root.x)

    # increment pathLen by 1
    pathLen = pathLen + 1

    if root.left is None and root.right is None:
        # leaf node then print the list
        paths_list.append(pathLen-1)
    else:
        # try for left and right subtree
        pathsRec(root.left, path, pathLen)
        pathsRec(root.right, path, pathLen)
            

node = Node(314)
node.left = Node(6)
node.left.left = Node(271)
node.right = Node(6)
node.right.left = Node(2)
node.right.left.right = Node(1)
node.right.right = Node(271)

pathsRec(node)
average = sum(paths_list)/len(paths_list)
print(average)
# print(height(node))
# print_nodes_iter_bfs(node)
# print_nodes_iter_dfs(node)
# print_nodes_recursion(node)