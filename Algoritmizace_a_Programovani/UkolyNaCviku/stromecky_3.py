def nacist_hodnoty():
    i = 2
    vals = []
    while i >= 1:
        vals.append(int(input()))
        i-=1
    if any((y < 1) or (y > 20) for y in vals):
        return(None, None)
    return(vals)


def stromecek(k, l):
    # if k < 2:
    #     return
    # pocet tecek
    m = k -1
    star_cntr = 0
 
    # vnejsi smycka - pocet radku stromecku
    for i in range(0, k):
        hvezdicek = (i + 1 + star_cntr)
     
        # vyteckuj do prvni hvezdicky
        print("." * m, end="")

        # vytiskni hvezdicky
        print("*" * (i + 1 + star_cntr), end="")

        # vyteckuj po posledni hvezdicce do konce
        print("." * m, end="")
        
        # sniz k a star counter
        m -= 1
        star_cntr += 1

        # novy radek
        print("\r")
    
    for i in range(l):
        dots = "." * (hvezdicek//2)
        print(f"{dots}*{dots}")
 

if __name__ == "__main__":
    vstup = nacist_hodnoty()
    k = l = 0
    if any(y is not None for y in vstup):
        k, l = vstup
        stromecek(k, l)
