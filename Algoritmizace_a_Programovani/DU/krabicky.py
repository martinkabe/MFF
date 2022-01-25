# Určete seznam čísel z intervalu 200..300, která nelze vytvořit z čísel 2 4 5 7 a operací + + * * (dvě sčítání a dvě násobení).

# Každou hodnotu, výchozí i vypočtenou, můžete použít, kolikrát chcete.

# Každou operaci můžete použít jenom jednou, tedy v tomto případě můžete (a nemusíte) použít maximálně dvě sčítání a maximálně dvě násobení.

# Jak se vytvářejí čísla, si můžete vyzkoušet na https://atest.geometry.cz/.

# Jako odpověď odevzdejte text obsahující

# seznam čísel, která nelze vytvořit
# popis, jak jste své řešení našli.

from itertools import permutations

def je_nesestrojitelna_hodnota(target):
    numbers   = ["2","4","5","7"]
    operators = ["+","+","*","*"]
    for values in permutations(numbers,len(numbers)):
        for oper in permutations(operators,len(numbers)-1):
            formula = "".join(o+v for o,v in zip([""]+list(oper),values))
            if eval(formula) == target:
                return False
    return True

nesestrojitelna_cisla = []
for cislo in range(200, 301):
    if je_nesestrojitelna_hodnota(cislo):
        nesestrojitelna_cisla.append(cislo)

print(*nesestrojitelna_cisla, end=" ")