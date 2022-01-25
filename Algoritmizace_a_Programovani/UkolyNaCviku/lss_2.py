class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def PrintLinkedList( p ):
    print( "LSS:", end=" " )
    while p!=None:
        print( p.data, end=" " )
        p = p.next
    print(".")

def ReadLinkedList():
    """cte cisla z radku, dokud nenacte prazdny row"""
    first = None
    last = None
    r = input()
    while r!="":
        row = r.split()
        if len(row)==0: # protoze ten test r!="" v RCDdata neukoncil cyklus!
            break
        for s in row:
            p = Node(int(s),None)
            if first==None:
                first = p
            else:
                last.next = p
            last = p
        r = input()
    return first

#################################################

def IntersectionDestruct(a,b):
    head = tail = None
 
    # once one or the other list runs out — we are done
    while a and b:
 
        if a.data == b.data:
            if head is None:
                head = Node(a.data, head)
                tail = head
            else:
                tail.next = Node(a.data, tail.next)
                tail = tail.next
 
            a = a.next
            b = b.next
 
        # advance the smaller list
        elif a.data < b.data:
            a = a.next
        else:
            b = b.next
 
    return head    

#################################################

PrintLinkedList( IntersectionDestruct( ReadLinkedList(), ReadLinkedList() ) )
