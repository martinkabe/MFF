from typing import List

## variace bez opakovani
def vars(items, k): 
    if k==0: 
        yield [] 
    else: 
        for item in items: 
            for v in vars(items, k-1): 
                if item not in v: 
                    yield [item] + v 

vars = vars(["a", "b", "c"], 2)
print(*vars)

## variace s opakovanim
def variations_with_repeating(lst: List, k):
    l = []
    for i in range(pow(len(lst), k)):
        o = []
        for j in range(k):
            o.append(lst[i % len(lst)])
            i = i // len(lst)
        l.append(o)
    return l

k = 3
a = [1,2,3,4,5]
vars = variations_with_repeating(a, k)
print(vars)