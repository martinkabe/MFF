from typing import List

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

def walk_recursive(root: Node) -> None:
    if root is None:
        return
    else:
        print(root.data, end=" ") # pre-order traversal
        walk_recursive(root.left)
        # print(root.data, end=" ") # in-order traversal
        walk_recursive(root.right)
        # print(root.data, end=" ") # post-order traversal

def walk_iterative(root: Node, stack: List = []) -> None:
    stack.append(root)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node.data, end=" ")
            stack.append(node.right)
            stack.append(node.left)


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
 
    walk_recursive(root)
    # walk_iterative(root)