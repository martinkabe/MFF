class Lahev(object):

    @property
    def objem(self):
        return self._objem

    @objem.setter
    def objem(self, value):
        self._objem = value

    @property
    def stav(self):
        return self._stav

    @stav.setter
    def stav(self, value):
        self._stav = value

    def __init__(self, objem):
        self._objem = 0
        self._stav = 0
        self.objem = objem

    def KolikJeVolno(self):
        return (self.objem - self.stav)

    def Prilij(self, kolik):
        if (self.KolikJeVolno() < kolik):
            raise Exception("Prelevas moc!")
        self.stav += kolik

    def Odlij(self, kolik):
        if (self.stav < kolik):
            raise Exception("Prelevas moc!")
        self.stav -= kolik


class Stav(object):

    @property
    def lahve(self):
        return self._lahve

    @lahve.setter
    def lahve(self, value):
        self._lahve = value

    @property
    def pocetKroku(self):
        return self._pocetKroku

    @pocetKroku.setter
    def pocetKroku(self, value):
        self._pocetKroku = value

    def __init__(self, lahve, pocetKroku):
        self._lahve = 0
        self._pocetKroku = 0
        self.lahve = []
        i = 0
        while (i < len(lahve)):
            self.lahve.append(Lahev(lahve[i].objem))
            self.lahve[i].Prilij(lahve[i].stav)
            i += 1
        self.pocetKroku = pocetKroku

    def GetHash(self):
        stavy = []
        i = 0
        while (i < len(self.lahve)):
            stavy.append(str(self.lahve[i].stav))
            i += 1
        return "-".join(map(str, stavy))

    def ProzkoumejSe(self):
        ProzkoumaneStavy.Add(self)

        for i in range(len(self.lahve)):
            NalezeneObjemy.Add(self.lahve[i].stav, self.pocetKroku)
        
        for i in range(len(self.lahve)):
            if (self.lahve[i].stav == 0):
                continue

            for j in range(len(self.lahve)):
                if (i == j):
                    continue

                novy = Stav(self.lahve, (self.pocetKroku + 1))
                prelilJsemNeco = novy.prelij(novy.lahve[i], novy.lahve[j])
                if (not prelilJsemNeco):
                    continue
                if  ProzkoumaneStavy.Contains(novy):
                    continue
                Program.fronta.append(novy)
            

    def prelij(self, od, kam):
        kolikPreliju = (kam.KolikJeVolno() if ((kam.KolikJeVolno() < od.stav)) else od.stav)
        if (kolikPreliju == 0):
            return False
        od.Odlij(kolikPreliju)
        kam.Prilij(kolikPreliju)
        return True


class NalezeneObjemy(object):
    objemy = []
    poctyKroku = []

    @classmethod
    def Add(cls, objem, pocetKroku):
        if objem in cls.objemy:
            if (cls.poctyKroku[cls.objemy.index(objem)] <= pocetKroku):
                return
        cls.objemy.append(objem)
        cls.poctyKroku.append(pocetKroku)
    
    @classmethod
    def Vytiskni(cls):
        cls.seradit()
        i = 0
        while (i < len(cls.objemy)):
            print(f"{cls.objemy[i]}:{cls.poctyKroku[i]}", end=" ")
            i += 1

    @classmethod
    def seradit(cls):
        i = 0
        while (i < (len(cls.objemy) - 1)):
            j = 0
            while (j < (len(cls.objemy) - 1)):
                if (cls.objemy[j] > cls.objemy[(j + 1)]):
                    x = cls.objemy[j]
                    cls.objemy[j] = cls.objemy[(j + 1)]
                    cls.objemy[(j + 1)] = x
                    x = cls.poctyKroku[j]
                    cls.poctyKroku[j] = cls.poctyKroku[(j + 1)]
                    cls.poctyKroku[(j + 1)] = x
                j += 1
            i += 1


class ProzkoumaneStavy(object):
    prozkoumano = []

    @classmethod
    def Add(cls, s):
        cls.prozkoumano.append(s.GetHash())

    @classmethod
    def Contains(cls, s):
        return s.GetHash() in cls.prozkoumano


class NactiData:
    @staticmethod
    def nacteni_dat():
        Va, Vb, Vc, Sa, Sb, Sc = list(map(int, input().split()))
        return [Va, Vb, Vc], [Sa, Sb, Sc]


class Program(object):
    fronta = []

    @classmethod
    def Main(cls):
        lahve = []
        objemy, obsahy = NactiData.nacteni_dat()

        if all(i <= 10 for i in objemy): # zadny z objemu neni vetsi nez 10
            for i in range(len(objemy)):
                lahve.append(Lahev(objemy[i]))

            for i in range(len(obsahy)):
                lahve[i].Prilij(obsahy[i])

            cls.fronta.append(Stav(lahve, 0))

            while (len(cls.fronta) > 0):
                prvniStav = cls.fronta[0]
                cls.fronta.remove(prvniStav)
                prvniStav.ProzkoumejSe()

            NalezeneObjemy.Vytiskni()


if __name__ == '__main__':
    Program.Main()

# 4 1 1  1 1 1
# 0:1 1:0 2:1 3:2

# 5 5 5  3 2 2
# 9 8 7  5 4 3