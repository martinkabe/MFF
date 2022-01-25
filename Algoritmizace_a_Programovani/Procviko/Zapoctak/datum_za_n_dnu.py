
dny_v_mesici = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def nacti_vstupy():
    d, m, r = list(map(int, input().split()))
    pocet_dni = int(input())
    return d, m, r, pocet_dni

def je_prestupny_rok(rok):
    if (rok % 400 == 0) and (rok % 100 == 0):
        return True
    elif (rok % 4 ==0) and (rok % 100 != 0):
        return True
    else:
        return False

def urci_datum(d, m, r, pocet_dni):
    pocet_dni_v_mesici = dny_v_mesici[m-1]
    if m == 2 and je_prestupny_rok(r):
        pocet_dni_v_mesici = 29
    diff = pocet_dni_v_mesici - d

    if (pocet_dni + d) < pocet_dni_v_mesici and diff > pocet_dni:
        pocet_dni += d
    else:
        pocet_dni -= diff
        if pocet_dni == 0:
            pocet_dni = d + diff
        else:
            m += 1
            if m > 12:
                m = 1
                r += 1
            
            while pocet_dni >= pocet_dni_v_mesici:
                pocet_dni_v_mesici = dny_v_mesici[m-1]
                if m == 2 and je_prestupny_rok(r):
                    pocet_dni_v_mesici = 29
                pocet_dni -= pocet_dni_v_mesici
                m +=  1
                if m > 12:
                    m = 1
                    r += 1
    
    if pocet_dni <= 0:
        pocet_dni = dny_v_mesici[m-2] + pocet_dni
        m -= 1

    if pocet_dni == 29 and not je_prestupny_rok(r):
        m += 1
        pocet_dni = 1
    
    if m == 0:
        m = 12
        r -= 1
    
    return [pocet_dni, m, r]


if __name__=="__main__":
    d, m, r, pd = nacti_vstupy()
    if d <= 31 and m <= 12 and pd >= 0:
        datum = urci_datum(d, m, r, pd)
        print(*datum, end=" ")
