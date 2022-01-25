import sys
from typing import List


def print_vysledek(dct_counters: dict, dct_pos: dict) -> None:
    max_hodnota = -sys.maxsize - 1
    cntr = 0
    for key, value in dct_counters.items():
        if key > max_hodnota and value == 1:
            max_hodnota = key
            cntr += 1
    if cntr == 1:
        print(f"{max_hodnota} {dct_pos[max_hodnota]}")
    else:
        print(None)

def urci_max_neopakujicise_hodnotu(arr: List) -> None:
    collector = {}
    collector_pos = {}
    arr_len = len(arr)

    for i in range(arr_len):
        if arr[i] in collector:
            collector[arr[i]] += 1
        else:
            collector[arr[i]] = 1
            collector_pos[arr[i]] = i
    
    print_vysledek(collector, collector_pos)


arr = [2,2,6,1,1,7,9,2,5,7,9,6]
urci_max_neopakujicise_hodnotu(arr)