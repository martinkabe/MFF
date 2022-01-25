from typing import List

def permut(lst: List):
    if not lst:
        return []
    
    if len(lst) == 1:
        return [lst]
    
    l = []
    for i in range(len(lst)):
        m = lst[i]
        o = lst[:i] + lst[i+1:]
        for j in permut(o):
            l.append([m] + j)
    return l


a = [1,2,3]
p = permut(a)
print(p)