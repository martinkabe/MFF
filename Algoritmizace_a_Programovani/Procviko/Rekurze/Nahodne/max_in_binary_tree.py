class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def find_max(root):
    # base case
    if root == None:
        return float("-inf")
    
    res = root.data
    l_res = find_max(root.left)
    r_res = find_max(root.right)

    res = max(res, l_res, r_res)

    return res

if __name__ == '__main__':
    root = Node(2)
    root.left = Node(7)
    root.right = Node(5)
    root.left.right = Node(6)
    root.left.right.left = Node(1)
    root.left.right.right = Node(11)
    root.right.right = Node(9)
    root.right.right.left = Node(4)
 
    # Function call
    print("Maximum element is",
          find_max(root))
