# https://leetcode.com/problems/different-ways-to-add-parentheses/
from typing import List

def diffWaysToCompute(expression: str) -> List:
    def dp(s):
        res=[]
        for i in range(len(s)):
            if '+' not in s and '*' not in s:
                return [int(s)]
            if s[i] in ('+','*'):
                L1=dp(s[:i])
                L2=dp(s[i+1:])
                if s[i]=='+':
                    for x in L1:
                        for y in L2:
                            res.append(x+y)
                elif s[i]=='*':
                    for x in L1:
                        for y in L2:
                            res.append(x*y)
        return res
    return dp(expression)


from itertools import permutations

def je_nesestrojitelna_hodnota(target: int) -> bool:
    numbers   = ["2","4","5","7"]
    operators = ["+","+","*","*"]
    for values in permutations(numbers,len(numbers)):
        for oper in permutations(operators,len(numbers)-1):
            formula = "".join(o+v for o,v in zip([""]+list(oper),values))
            # print(formula)
            formula_with_brackets = diffWaysToCompute(formula)
            if target in formula_with_brackets:
                return False
    return True

nesestrojitelna_cisla = []
for cislo in range(200, 301):
    if je_nesestrojitelna_hodnota(cislo):
        nesestrojitelna_cisla.append(cislo)

print(*nesestrojitelna_cisla, end=" ")

# 1. {200..300}\{210}
# 2. a) Hruba sila -> vyrobil jsem vsechny permutace z cisel [2,4,5,7] a k nim mozne zpusoby, jak roztridit operators-1 aritmetickych operatoru tak,
# abych pouzil maximalne dve scitani a dve nasobeni.
#    b) funkce diffWaysToCompute vrati list vysledku, kdyz budu ruzne permutovat zavorky ve vyrazu
#    c) pak uz jen tyto hodnoty porovnam s tou referencni, resp. [200..300] ve smycce

# Kod neni vubec optimalizovany, jen rychly nacrt toho, jak bych postupoval