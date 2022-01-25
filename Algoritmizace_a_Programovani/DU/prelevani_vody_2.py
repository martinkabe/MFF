x = y = z = 0

def tisk_vystup(vysledky:dict):
    for key, value in vysledky.items():
        if value != -1:
            print(f"{key}:{value}", end=" ")

def nacteni_dat() -> list:
    global x, y, z
    Va, Vb, Vc, Sa, Sb, Sc = list(map(int, input().split()))
    x, y, z = Va, Vb, Vc
    return [Sa, Sb, Sc]

def nacteni_konfigurace(obsahy:list) -> dict:
    konfigurace = {}
    max_mozny_obsah = max(x, y, z) if sum(obsahy) > max(x, y, z) else sum(obsahy)
    for obsah in range(0, max_mozny_obsah + 1):
        konfigurace[obsah] = 0
    return(konfigurace)

def prelevej(obsahy:list, konfigurace:dict) -> dict:
    a, b, c = obsahy
    for key, value in konfigurace.items():
        cntr = 0
        obsahy_nove = obsahy.copy()

        if key in obsahy_nove:
            konfigurace[key] = cntr
            continue

        # prelej do a
        if (a+b) <= x:
            obsahy_nove[0] = a + b
            obsahy_nove[1] -= b
            if key in obsahy_nove:
                konfigurace[key] = 1
                continue
        if (a+c) <= x:
            obsahy_nove[0] = a + c
            obsahy_nove[2] -= c
            if key in obsahy_nove:
                konfigurace[key] = 1
                continue
        if (a+b+c) <= x:
            obsahy_nove[0] = a + b + c
            obsahy_nove[1] -= b
            obsahy_nove[2] -= c
            if key in obsahy_nove:
                konfigurace[key] = 2
                continue
        
        # prelej do b
        if (b+a) <= y:
            obsahy_nove[1] = b + a
            obsahy_nove[0] -= a
            if key in obsahy_nove:
                konfigurace[key] = 1
                continue
        if (b+c) <= y:
            obsahy_nove[1] = b + c
            obsahy_nove[2] -= c
            if key in obsahy_nove:
                konfigurace[key] = 1
                continue
        if (a+b+c) <= y:
            obsahy_nove[1] = a + b + c
            obsahy_nove[0] -= a
            obsahy_nove[2] -= c
            if key in obsahy_nove:
                konfigurace[key] = 2
                continue
        
        # prelej do c
        if (a+c) <= z:
            obsahy_nove[2] = a + c
            obsahy_nove[0] -= a
            if key in obsahy_nove:
                konfigurace[key] = 1
                continue
        if (b+c) <= z:
            obsahy_nove[2] = b + c
            obsahy_nove[1] -= b
            if key in obsahy_nove:
                konfigurace[key] = 1
                continue
        if (a+b+c) <= z:
            obsahy_nove[2] = a + b + c
            obsahy_nove[0] -= a
            obsahy_nove[1] -= b
            if key in obsahy_nove:
                konfigurace[key] = 2
                continue
        
        konfigurace[key] = -1

    return konfigurace


if __name__ == "__main__":
    Sabc = nacteni_dat()
    if all(i <= 10 for i in Sabc):
        konfigurace = nacteni_konfigurace(Sabc)
        vystup = prelevej(Sabc, konfigurace)
        tisk_vystup(vystup)

# 4 1 1  1 1 1
# 0:1 1:0 2:1 3:2

# 5 5 5  3 2 2
# 9 8 7  5 4 3