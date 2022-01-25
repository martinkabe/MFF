
PocetPorovnani = 0
def JeTezsi(a, b):
    global PocetPorovnani
    PocetPorovnani += 1
    return a > b

def DruhaNeboPata(a, b, c, d, e, f):
    # Potrebujeme 9 porovnani v nejhorim pripade, abychom nasli 2. nejlehci kastan
    # tzn. a->b, a->c, ..., a->f, b->c, b->d, b->f
    
    # Moje nize uvedene reseni funguje na 7 porovnani, abychom nasli 2. nejlehci kastan
    # tzn. rozdelim na dvojice (a, b), (c, d), (e, f) a z nich vyberu minumum
    if JeTezsi(a, b):
        a, b = b, a
    if JeTezsi(c, d):
        c, d = d, c
    if JeTezsi(e, f):
        e, f = f, e
    
    # Ze vsech minimalnich prvku vyberu ten nejmensi a ulozim do a
    if JeTezsi(a, c):
        a, c = c, a
    if JeTezsi(a, e):
        a, e = e, a

    # Pak uz jen porovnam prvky, ktere jsem v predchozich krocich porovnaval s timto nejmejsim prvkem
    # a znich vyberu minimum, coz bude muj hledany 2. nejlehci kastan
    if JeTezsi(b, c):
        b, c = c, b
    if JeTezsi(b, e):
        b, e = e, b
    
    print(f"Pocet porovnani = {PocetPorovnani}")
    return b

## Testove pripady
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
# print(DruhaNeboPata(10, 9, 8, 7, 100, 5))