# Tree node
class Node:
    def __init__(self , key):
        self.value = key 
        self.left = None
        self.right = None

def minDepth(root):
    # Corner Case.Should never be hit unless the code is 
    # called on root = NULL
    if root is None:
        return 0 
    
    # Base Case : Leaf node.This accounts for height = 1
    if root.left is None and root.right is None:
        return 1
    
    # If left subtree is Null, recur for right subtree
    if root.left is None:
        return minDepth(root.right)+1
    
    # If right subtree is Null , recur for left subtree
    if root.right is None:
        return minDepth(root.left) +1 
    
    return min(minDepth(root.left), minDepth(root.right))+1

# O(N)
def PrintLeafNodes(root, level):
    if (root == None):
        return
  
    if (level == 1):
        if (root.left == None and root.right == None):
            print(root.value, end = " ")
     
    elif (level > 1):
        PrintLeafNodes(root.left, level - 1)
        PrintLeafNodes(root.right, level - 1)

# Driver Program
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

min_depth = minDepth(root)
PrintLeafNodes(root, min_depth)