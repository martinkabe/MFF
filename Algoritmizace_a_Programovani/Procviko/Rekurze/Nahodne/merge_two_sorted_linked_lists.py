from typing import List

class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def print_linked_list(self, node: Node) -> None:
        curr = node
        while curr:
            print(curr.data)
            curr = curr.next
    
    def sorted_merge(self, A:Node, B:Node) -> Node:
        if A is None: return B
        if B is None: return A

        if A.data < B.data:
            A.next = self.sorted_merge(A.next, B)
            return A
        else:
            B.next = self.sorted_merge(A, B.next)
            return B

n1 = Node(1, Node(8, Node(22, Node(40))))
n2 = Node(4, Node(11, Node(16, Node(20))))
ll = LinkedList()
merged_list = ll.sorted_merge(n1, n2)
ll.print_linked_list(merged_list)