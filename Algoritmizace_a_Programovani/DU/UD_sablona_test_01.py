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


#################################################

def UnionDestruct(a, b):
    """ destruktivni sjednoceni dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """

    headA = a
    headB = b

    if headA.x <= headB.x:
        tail = headA
        headA = headA.dalsi
    else:
        tail = headB
        headB = headB.dalsi
    
    head = tail

    while True:
        if headA is None:
            tail.dalsi = headB
            break
        if headB is None:
            tail.dalsi = headA
            break

        if headA.x <= headB.x:
            tail.dalsi = headA
            headA = headA.dalsi
        else:
            tail.dalsi = headB
            headB = headB.dalsi
        
        tail = tail.dalsi
    
    return head

#################################################

VytiskniLSS( UnionDestruct( NactiLSS(), NactiLSS() ) )