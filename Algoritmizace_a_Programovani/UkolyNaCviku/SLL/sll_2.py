
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def remove_node(self, value):
        current = self.head
        while current:
            if current.next.data == value:
                current.next = current.next.next
                break
            current = current.next

    def append_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def append_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    sll = LinkedList()

    sll.append_end(5)
    sll.append_end(8)
    sll.append_end(10)
    sll.append_end(11)
    sll.append_beginning(-5)

    sll.remove_node(10)

    sll.print_list()