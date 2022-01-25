from typing import Tuple

def zisk(vyradim_souperu, z_kolika):
    # 100.000,- * v / p
    return(100000 * vyradim_souperu/z_kolika)


def pocitej_zisk(komb: Tuple):
    souperu_celkem = 100
    zisk_sum = 0

    for k in komb:
        zisk_sum += int(zisk(k, souperu_celkem))
        souperu_celkem -= k
    return(zisk_sum)


def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


def vrat_vysledek():
    kol = int(input())

    L = list(sums(kol, 100))
    D = {}
    for k in L:
        if 0 not in k:
            D[k] = pocitej_zisk(k)

    max = 0
    komb = [(), 0]
    for key, val in D.items():
        if val > max:
            komb[0] = key
            komb[1] = val
            max = val

    print(komb[1])
    print(' '.join(map(str, komb[0])))


if __name__ == '__main__':
    vrat_vysledek()