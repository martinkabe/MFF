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

def UnionDestruct(a,b):
    """ destruktivni sjednoceni dvou usporadanych seznamu
    * nevytvari zadne nove prvky, vysledny seznam bude poskladany z prvku puvodnich seznamu,
    * vysledek je MNOZINA, takze se hodnoty neopakuji """

    r = None
    head = None
    last = None
    
    while True:
        if a is None and b is None:
            break
        
        if b is None or a is not None and a.x <= b.x:
            if last is None or last < a.x:
                if r is None:
                    r = a
                    head = r
                else:
                    r.dalsi = a
                    r = r.dalsi
            last = a.x
            a = a.dalsi
        elif a is None or b.x < a.x:
            if last is None or last < b.x:
                if r is None:
                    r = b
                    head = r
                else:
                    r.dalsi = b
                    r = r.dalsi
            last = b.x
            b = b.dalsi

    return head

#################################################

VytiskniLSS( UnionDestruct( NactiLSS(), NactiLSS() ) )
