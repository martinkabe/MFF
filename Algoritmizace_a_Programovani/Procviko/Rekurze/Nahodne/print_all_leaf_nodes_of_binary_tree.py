class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

def printLeafNodes(root: Node) -> None:
    if root is None: return
    if root.left is None and root.right is None:
        print(root.data, end=" ")
        return
    if root.left is not None:
        printLeafNodes(root.left)
    if root.right is not None:
        printLeafNodes(root.right)


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
 
    # print leaf nodes of the given tree
    printLeafNodes(root)