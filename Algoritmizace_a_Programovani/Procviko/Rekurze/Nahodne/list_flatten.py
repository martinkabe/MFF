from typing import List


def list_to_flatten(lst: List, arr_glob: List = []) -> List:
    for l in lst:
        if type(l) == int:
            arr_glob.append(l)
        elif type(l) == list:
            list_to_flatten(l, arr_glob)
    return arr_glob

arr = list_to_flatten([1, [3,5,7], 3, [2,[4,[6,8,10]]]], [])
print(arr)