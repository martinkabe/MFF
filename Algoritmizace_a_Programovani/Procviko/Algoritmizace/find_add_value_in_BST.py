class RootNode:
    def __init__(self, x, left=None, right=None):
        self.x = x
        self.left = left
        self.right=right

def searchElement_iter(root:RootNode, target: int) -> RootNode:
    while root is not None and root.x != target:
        if target < root.x:
            root = root.left
        else:
            root = root.right
    return root

def searchElement_recursive(root:RootNode, target: int) -> RootNode:
    if root is None:
        return None
    elif root.x == target:
        return root
    elif target < root.x:
        return searchElement_recursive(root.left, target)
    else:
        return searchElement_recursive(root.right, target)

def add_value_recursive(root: RootNode, x: int) -> bool:
    if root is None:
        root = RootNode(x)
    elif x < root.x:
        root = add_value_recursive(root.left, x)
    elif x > root.x:
        root = add_value_recursive(root.right, x)
    return root


node = RootNode(50)
node.left = RootNode(25)
node.left.left = RootNode(12)
node.left.left.left = RootNode(6)
node.left.right = RootNode(41)
node.right = RootNode(77)
node.right.left = RootNode(63)
node.right.left.left = RootNode(56)
node.right.left.left = RootNode(53)
node.right.right = RootNode(90)
node.right.right.right = RootNode(95)
node.right.right.right.right = RootNode(99)
node.right.right.left = RootNode(84)
node.right.right.right.left = RootNode(94)

p = add_value_recursive(node, 80)
print(p)

# searched_node = searchElement_recursive(node, 84)
# searched_node = searchElement_iter(node, 84)
# print(searched_node.x)