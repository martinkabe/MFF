
PocetPorovnani = 0
def JeTezsi(a, b):
    global PocetPorovnani
    PocetPorovnani += 1
    return a > b


def DruhaNeboPata(a, b, c, d, e, f):
    # Potrebujeme 9 porovnani v nejhorim pripade, abychom nasli 2. nejlehci kastan
    a_premisteno = False
    if JeTezsi(a, d):
        a, d = d, a
        a_premisteno = True
    if JeTezsi(b, e):
        b, e = e, b
    if JeTezsi(c, f):
        c, f = f, c
    if JeTezsi(b, c):
        b, c = c, b
        e, f = f, e
    if a_premisteno:
        if JeTezsi(b, c):
            b, c = c, b
        if JeTezsi(b, d):
            b, d = d, b
        print(f"Pocet porovnani = {PocetPorovnani}")
        return b
    else:
        if JeTezsi(a, b):
            a, b = b, a
        if JeTezsi(c, d):
            c, d = d, c
        if JeTezsi(b, c):
            b, c = c, b
    if JeTezsi(b, e):
        b, e = e, b
    print(f"Pocet porovnani = {PocetPorovnani}")
    return b


# print(DruhaNeboPata(16, 17, 30, 22, 20, 100))
# print(DruhaNeboPata(18, 17, 30, 22, 20, 1))
# print(DruhaNeboPata(18, 17, 30, 22, 20, 100))
# print(DruhaNeboPata(18, 17, 30, 22, 20, 1))
# print(DruhaNeboPata(1, 17, 30, 22, 20, 18))
# print(DruhaNeboPata(1, 19, 30, 22, 20, 18))
# print(DruhaNeboPata(20, 19, 30, 22, 21, 18))
# print(DruhaNeboPata(20, 25, 30, 17, 21, 26))
# print(DruhaNeboPata(20, 25, 30, 22, 21, 26))
# print(DruhaNeboPata(1, 2, 3, 4, 5, 6))
# print(DruhaNeboPata(10, 2, 13, 20, 5, 6))
# print(DruhaNeboPata(10, 2, 13, 20, 5, 1))
print(DruhaNeboPata(10, 9, 8, 7, 6, 5))