from collections import deque
from tree_utils import TreeUtilities as tu

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def maxDepth_recursive(root: Node):
    if not root:
        return -1
    return 1 + max(maxDepth_recursive(root.left), maxDepth_recursive(root.right))

def maxDepth_BFS(root: Node):
    if not root:
        return -1

    level = 0
    q = deque([root])
    while len(q) > 0:
        for _ in range(len(q)):
            node = q.popleft()
            print(f"Node: {node.data}")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
        print("------------------")
    return level

def maxDepth_DFS(root: Node):
    if not root:
        return 0
    
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()
        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res

n = Node("F")
n.left = Node("D")
n.left.left = Node("B")
n.left.right = Node("E")
n.left.left.left = Node("A")
n.left.left.right = Node("C")
n.right = Node("J")
n.right.right = Node("K")
n.right.left = Node("G")
n.right.left.right = Node("I")
n.right.left.right.left = Node("H")

# tu.topview(n)

print(maxDepth_DFS(n))
# print(maxDepth_recursive(n))