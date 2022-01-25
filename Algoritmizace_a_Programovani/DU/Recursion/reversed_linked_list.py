class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printLL(self, node):
        if self.head is None:
            self.head = node
        
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
    
    def printReverseOrder(self, node):
        if node is None:
            return
        self.printReverseOrder(node.next)
        print(node.data)
    
    def printLastButOneNode(self, node):
        if self.head is None:
            self.head = node
        
        curr = self.head
        while curr.next.next is not None:
            curr = curr.next
        print(curr.data)


p = Node(10, Node(20, Node(30, Node(40))))
ll = LinkedList()
ll.printLL(p)
print("------ Reverse order --------")
ll.printReverseOrder(p)
print("------ Print last but one node --------")
ll.printLastButOneNode(p)