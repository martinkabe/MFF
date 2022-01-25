
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

llist = LinkedList()
llist.append(2)
llist.append(5)
llist.append(8)
llist.append(10)

llist.print_linked_list()