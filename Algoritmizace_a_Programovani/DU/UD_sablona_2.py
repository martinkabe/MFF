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

    head = a
    while head.dalsi:
        head = head.dalsi
    head.dalsi = b

    head = a
    delete_duplicates(head)

    return a

#################################################

VytiskniLSS( UnionDestruct( NactiLSS(), NactiLSS() ) )
