
PocetPorovnani = 0
def JeTezsi(a, b):
    global PocetPorovnani
    PocetPorovnani += 1
    return a > b

def DruhaNeboPata_1(a, b, c, d, e, f):
    # Potrebujeme 9 porovnani v nejhorim pripade, abychom nasli 2. nejlehci kastan
    # tzn. 
    # a->b, a->c, ..., a->f => 5 porovnani
    # b->c, b->d, b->e, b->f => 4 porovnani
    # celkem tedy 9 porovnani
    
    # Nize uvedene reseni funguje na 7 porovnani, abychom nasli 2. nejlehci kastan
    # (v tomto reseni se ciste zamerim na nalezeni 2. nejlehciho kastanu!)
    # tzn. rozdelim na dvojice (a, b), (c, d), (e, f) a z nich vyberu minima z tech porovnavanych dvojic
    # a ulozim do promennych a, c, e
    if JeTezsi(a, b):
        a, b = b, a
    if JeTezsi(c, d):
        c, d = d, c
    if JeTezsi(e, f):
        e, f = f, e
    # Ze vsech tech minimalnich prvku vyberu minimum a ulozim do a
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
    # Vytisknu pocet pozorovani a vratim druhy nejlehci kastan
    print(f"Pocet porovnani = {PocetPorovnani}")
    return b


def DruhaNeboPata_2(a, b, c, d, e, f):
    # Nase horni hranice pro nejhorsi pripad je tedy 9 porovnani potrebnych k tomu, abychom
    # zjistili druhy nejlehci kastan (popis viz vyse ve funkci DruhaNeboPata_1())

    # Reseni nize funguje v nejhorsim pripade pro 7 porovnani a
    # v nejlepsim pripade pro 5 porovnani

    # Nejprve setridim kastany (a, b, c)
    if JeTezsi(a, b):
        a, b = b, a
    if JeTezsi(b, c):
        b, c = c, b
        if JeTezsi(a, b):
            a, b = b, a
    # b ted urcite nebude nejtezsi a ani nejlehci
    # b tedy porovnam se zbytkem kastanu, tedy s d, e, f
    c4 = JeTezsi(b, d)
    c5 = JeTezsi(b, e)
    c6 = JeTezsi(b, f)
    if c4 == c5 == c6:  # Vsechny jsou True nebo vsechny jsou False, tedy b je hledany kastan
        print(f"Pocet porovnani = {PocetPorovnani}")
        return b
    if c4 ^ c5 ^ c6:  # Pouze jeden z nich je True (XOR), tedy b je vetsi nez pouze jeden z nich
                      # potom vx bude jeden z d, e, f, pro ktery je b vetsi
                      # vrat vetsi z a, vx
        vx = d if c4 else (e if c5 else f)
        print(f"Pocet porovnani = {PocetPorovnani}")
        return a if JeTezsi(a, vx) else vx
    else:  # Pouze jeden z nich je False (b je vetsi nez oba dva), potom vx bude jeden z d, e, f,
           # pro ktery neni b vetsi
           # vrat mensi z c a vx
        vx = d if not c4 else (e if not c5 else f)
        print(f"Pocet porovnani = {PocetPorovnani}")
        return vx if JeTezsi(c, vx) else c


## Testove pripady, pro ktere jsem validoval vyse uvedene pristupy:
# print(DruhaNeboPata(16, 17, 30, 22, 20, 100))
# print(DruhaNeboPata(18, 17, 30, 22, 20, 1))
# print(DruhaNeboPata(18, 17, 30, 22, 20, 100))
# print(DruhaNeboPata(18, 17, 30, 22, 20, 1))
# print(DruhaNeboPata(1, 17, 30, 22, 20, 18))
# print(DruhaNeboPata(1, 19, 30, 22, 20, 18))
# print(DruhaNeboPata(20, 19, 30, 22, 21, 18))
# print(DruhaNeboPata(20, 25, 30, 17, 21, 26))
# print(DruhaNeboPata(20, 25, 30, 22, 21, 26))
# print(DruhaNeboPata_2(1, 2, 3, 4, 5, 6))
# print(DruhaNeboPata(10, 2, 13, 20, 5, 6))
# print(DruhaNeboPata_2(10, 2, 13, 20, 5, 1))
# print(DruhaNeboPata_2(10, 9, 8, 7, 100, 5))