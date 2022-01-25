# Rozklad cisla na soucet scitancu

def rozklady(n):
    def rozklad(i, zbytek):
        if zbytek == 0:
            print(r[1:i])
        else:
            for j in range(1, min(zbytek, r[i-1]) +1 ):
                r[i] = j
                rozklad(i+1, zbytek - j)

    r = [n] * (n+1)
    rozklad(1, n)

rozklady(5)
