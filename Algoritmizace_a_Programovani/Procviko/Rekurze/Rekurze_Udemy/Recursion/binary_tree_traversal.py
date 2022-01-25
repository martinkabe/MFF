from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def traverse_dfs(root: Node):
    stack = []
    stack.append(root)

    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node.data, end=" ")
            stack.append(node.left)
            stack.append(node.right)
            

def traverse_bfs(root: Node):
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        if node is not None:
            print(f"Node {node.data}")
            queue.append(node.left)
            queue.append(node.right)


def traverse_recursion(root: Node):
    if not root: return
     
    print(root.data)
    traverse_recursion(root.left)
    traverse_recursion(root.right)
    
def maxDepth(root: Node):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

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

print(maxDepth(n))

# traverse_recursion(n)
# traverse_bfs(n)
# traverse_dfs(n)