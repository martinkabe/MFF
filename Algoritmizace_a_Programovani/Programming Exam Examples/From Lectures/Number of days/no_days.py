
class Datum:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y


class DataReader:
    @staticmethod
    def nacti_data():
        d1, m1, y1, d2, m2, y2 = list(map(int, input().split()))
        return(Datum(d1, m1, y1), Datum(d2, m2, y2))


class KalendarovaKalkulacka:
    # dle dnu v kalendari leden-prosinec
    pocetDniMesicu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # pocet prestupnych roku pred zadanym datem
    def pocetPrestupnychRoku(d):
    
        roky = d.y
    
        # pokud je mesic zadaneho data do unora, nebudu zapocitavat do vypoctu prestupneho roku
        if (d.m <= 2):
            roky -= 1
    
        # rok je prestupny, pokud je nasobkem 4, nasobkem 400 a neni nasobkem 100
        return int(roky / 4) - int(roky / 100) + int(roky / 400)
    
    @classmethod
    def vypoctiCelkovyPocetDni(cls, d):
        # celkovy pocet dni pred zadanym datumem
    
        # inicializace prvniho datumu, resp. poctu dni
        n = d.y * 365 + d.d
    
        # doplnim predchozi mesice do aktualniho mesice - 1
        for i in range(0, d.m - 1):
            n += cls.pocetDniMesicu[i]
    
        # pocet prestupnych roku bude pricten k celkovemu poctu dni
        n += cls.pocetPrestupnychRoku(d)
        return n

    # metoda vraci pocet dni mezi zadanymi datumy
    @classmethod
    def rozdilDatumu(cls, dt1, dt2):

        n1 = cls.vypoctiCelkovyPocetDni(dt1)
        n2 = cls.vypoctiCelkovyPocetDni(dt2)
    
        # vrat rozdil mezi dvema pocty dni
        return (n2 - n1)


if __name__=="__main__":
    dt1, dt2 = DataReader.nacti_data()
    print(KalendarovaKalkulacka.rozdilDatumu(dt1, dt2))