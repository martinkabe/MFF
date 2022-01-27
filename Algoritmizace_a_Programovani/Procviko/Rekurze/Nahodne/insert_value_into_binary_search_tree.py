class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def insert_node(head: Node, data: int) -> Node:
    if head is None:
        head = Node(data)
        return head
    
    if head.data < data:
        head.right = insert_node(head.right, data)
    else:
        head.left = insert_node(head.left, data)
    
    return head


if __name__ == '__main__':
    root = Node(100)
    root.left = Node(80)
    root.left.left = Node(50)
    root.left.left.right = Node(60)
    root.left.left.left = Node(30)

    root.left.right = Node(90)
    root.left.right.left = Node(85)
    root.left.right.right = Node(95)

    root.right = Node(120)
    root.right.left = Node(110)
    root.right.left.right = Node(115)
    root.right.right = Node(140)
    root.right.right.right = Node(150)

    insert_node(root, 108)

    print(root)


    
