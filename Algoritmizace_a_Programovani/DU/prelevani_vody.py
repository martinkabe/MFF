zaznam = {}
kombinace = []
x = y = z = 0
cntr = 0
cntr_dict = {0:0, 1:0, 2:0, 3:0}

def nacteni_konfigurace() -> list:
    global x, y, z
    Va, Vb, Vc, Sa, Sb, Sc = list(map(int, input().split()))
    x, y, z = Va, Vb, Vc
    return (Sa, Sb, Sc)


def prelevej(obsahy:list):
    global cntr
    a, b, c = obsahy

    if (a, b, c) in zaznam:
        return False
    
    if a == 0 or b == 0 or c == 0:
        kombinace.append(obsahy)
        print(obsahy)
        return True
     
    zaznam[(a,b,c)] = cntr

    # vyprazdni nadobu a
    if a > 0:
        # vyprazdni a do b
        if (a + b) <= y:
            if prelevej((0, a + b, c)):
                cntr += 1
                kombinace.append(obsahy)
                return True
        else:
            if prelevej((a - (y - b), y, c)):
                cntr += 1
                kombinace.append(obsahy)
                return True
        # vyprazdni a do c
        if (a + c) <= z:
            if(prelevej((0, b, a + c)) ):
                cntr += 1
                kombinace.append(obsahy)
                return True
        else:
            if prelevej((a-(z-c), b, z)):
                cntr += 1
                kombinace.append(obsahy)
                return True
        
    # vyprazdni nadobu b
    if b > 0:
        # vyprazdni b do a
        if (a + b) <= x:
            if prelevej((a + b, 0, c)):
                cntr += 1
                kombinace.append(obsahy)
                return True
        else:
            if prelevej((x, b - (x - a), c)):
                cntr += 1
                kombinace.append(obsahy)
                return True
        # vyprazdni b do c
        if (b + c) <= z:
            if(prelevej((a, 0, b + c)) ):
                cntr += 1
                kombinace.append(obsahy)
                return True
        else:
            if prelevej((a, b - (z - c), z)):
                cntr += 1
                kombinace.append(obsahy)
                return True

    # vyprazdni nadobu c
    if c > 0:
        # vyprazdni c do a
        if (a + c) <= x:
            if prelevej((a + c, b, 0)):
                cntr += 1
                kombinace.append(obsahy)
                return True
        else:
            if prelevej((x, b, c - (x - a))):
                cntr += 1
                kombinace.append(obsahy)
                return True
        # vyprazdni c do b
        if (b + c) <= y:
            if prelevej((a, b + c, 0)):
                cntr += 1
                kombinace.append(obsahy)
                return True
        else:
            if prelevej((a, y, c - (y - b))):
                cntr += 1
                kombinace.append(obsahy)
                return True

    return False


if __name__ == "__main__":
    Sabc = nacteni_konfigurace()
    prelevej(Sabc)
    # vytiskni vysledky

# 4 1 1  1 1 1
# 0:1 1:0 2:1 3:2