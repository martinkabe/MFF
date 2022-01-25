# BFS https://www.youtube.com/watch?v=POpkdEdmlbU&list=RDCMUCovR8D97-8qmQ8hWQW0d3ew&index=2
# DFS https://www.youtube.com/watch?v=Sbciimd09h4&list=RDCMUCovR8D97-8qmQ8hWQW0d3ew&index=1

from typing import List
from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

# DFS
def walk_stack(tree: Node, stack: List):
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(f"popping {node.data}")
            stack.append(node.left)
            # print(f"appending {node.left}")
            stack.append(node.right)
            # print(f"appending {node.right}")

# BFS
def walk_queue(tree: Node):
    queue = deque()
    queue.appendleft(tree)
    while len(queue) > 0:
        node = queue.pop()
        if node is not None:
            print(f"popping {node.data}")
            queue.appendleft(node.left)
            # print(f"appending {node.left}")
            queue.appendleft(node.right)
            # print(f"appending {node.right}")

if __name__ == "__main__":
 
    # Let us create binary tree shown in
    # above diagram
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(8)
    root.right.left.left = Node(6)
    root.right.left.right = Node(7)
    root.right.right.left = Node(9)
    root.right.right.right = Node(10)
 
    walk_queue(root)
    # walk_stack(root, [])
    # walk_iterative(root)