class Prvek:
    def __init__(self, x, dalsi=None):
        self.x = x
        self.dalsi = dalsi

def VytiskniLSS( p ):
    print( "LSS:", end=" " )
    while p!=None:
        print( p.x, end=" " )
        p = p.dalsi
    print(".")

def NactiLSS():
    """cte cisla z radku, dokud nenacte prazdny radek"""
    prvni = None
    posledni = None
    r = input()
    while r!="":
        radek = r.split()
        if len(radek)==0: # protoze ten test r!="" v RCDX neukoncil cyklus!
            break
        for s in radek:
            p = Prvek(int(s),None)
            if prvni==None:
                prvni = p
            else:
                posledni.dalsi = p
            posledni = p
        r = input()
    return prvni

def delete_duplicates(head):
    current = head
    while current:
        runner = current
        # Zkontroluj, dokud runner.dalsi nebude None.
        while runner.dalsi:
            if current.x == runner.dalsi.x:
                runner.dalsi = runner.dalsi.dalsi
            else:
                runner = runner.dalsi
        current = current.dalsi

#################################################

def UnionDestruct(a,b):
    """ destruktivni sjednoceni dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """

    # A dummyNode k ukladani vysledku
    dummyNode = Prvek(0)
    headA = a
    headB = b
 
    # Tail Uklada posledni prvek
    tail = dummyNode
    while True:
 
        # If any of the list gets completely empty
        # directly join all the elements of the other list
        if headA is None:
            tail.dalsi = headB
            break
        if headB is None:
            tail.dalsi = headA
            break
 
        # Compare the x of the lists and whichever is smaller is
        # appended to the last of the merged list and the head is changed
        if headA.x <= headB.x:
            tail.dalsi = headA
            headA = headA.dalsi
        else:
            tail.dalsi = headB
            headB = headB.dalsi
 
        # Advance the tail
        tail = tail.dalsi
 
    # Returns the head of the merged list
    delete_duplicates(dummyNode.dalsi)
    return dummyNode.dalsi

#################################################

VytiskniLSS( UnionDestruct( NactiLSS(), NactiLSS() ) )
