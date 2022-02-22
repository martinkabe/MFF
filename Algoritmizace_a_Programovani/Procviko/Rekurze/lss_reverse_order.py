class Node:
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def print_ll(self, node):
        self.head = node
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
    
    def reverse_order(self, node):
        if node is None:
            return
        self.reverse_order(node.next)
        print(node.data)
    
    def reverse_order_new_ll(self, head):
        if head is None or head.next is None:
            return head
        p = self.reverse_order_new_ll(head.next)
        head.next.next = head
        head.next = None
        return p


node = Node(10, Node(20, Node(30, Node(40))))
ll = LinkedList()
print("----- PRINT LINKED LIST -----")
ll.print_ll(node)
print("----- PRINT LINKED LIST: REVERSED ORDER -----")
ll.reverse_order(node)
print("----- NEW NODE: REVERSED ORDER -----")
node_rev = ll.reverse_order_new_ll(node)
ll.print_ll(node_rev)