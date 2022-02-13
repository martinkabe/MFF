from collections import deque

class Bludiste:
    def __init__(self, bludiste_deska):
        self.bludiste_deska = bludiste_deska
        self.n = len(bludiste_deska)
        self.bludiste_navstiveno = [[False for _ in range(self.n)] for _ in range(self.n)]
        self.x_pohyb = [1, 0, -1, 0]
        self.y_pohyb = [0, 1, 0, -1]

    def spocti_min_pocet_kroku(self, start, cil, vzdalenost=0):
        fronta = deque()
        fronta.appendleft((start[0], start[1], vzdalenost))

        while len(fronta):
            krok = fronta.pop()
            self.bludiste_navstiveno[krok[0]][krok[1]] = True
            
            if krok[0] == cil[0] and krok[1] == cil[1]:
                return krok[2]
            
            for smer in range(len(self.x_pohyb)):
                x_novy = krok[0] + self.x_pohyb[smer]
                y_novy = krok[1] + self.y_pohyb[smer]

                if self.validni_krok(x_novy, y_novy):
                    fronta.appendleft((x_novy, y_novy, krok[2]+1))
        
        return -1
    
    def validni_krok(self, x, y):
        if x < 0 or x >= self.n:
            return False
        
        if y < 0 or y >= self.n:
            return False
        
        if self.bludiste_deska[x][y] == 0 or self.bludiste_navstiveno[x][y] == True:
            return False

        return True


if __name__ == '__main__':

    m = [[1,1,1,1,1],
        [0,0,0,0,1],
        [1,1,1,1,1],
        [1,0,0,0,0],
        [1,1,1,1,1]]
    
    bludiste = Bludiste(m)
    vysledek = bludiste.spocti_min_pocet_kroku((0,0),(4,4))
    print(f"Minimalni pocet kroku ze startu do cile je potreba udelat: {vysledek}")