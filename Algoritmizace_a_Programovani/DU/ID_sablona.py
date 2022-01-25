class Prvek:
    def __init__(self, x, dalsi = None):
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

def IntersectionDestruct(a,b):
    """ destruktivni prunik dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """

    head = tail = None
 
    # once one or the other list runs out — we are done
    while a and b:
 
        if a.x == b.x:
            if head is None:
                head = Prvek(a.x, head)
                tail = head
            else:
                tail.dalsi = Prvek(a.x, tail.dalsi)
                tail = tail.dalsi
 
            a = a.dalsi
            b = b.dalsi
 
        # advance the smaller list
        elif a.x < b.x:
            a = a.dalsi
        else:
            b = b.dalsi
 
    return head    

#################################################

VytiskniLSS( IntersectionDestruct( NactiLSS(), NactiLSS() ) )
