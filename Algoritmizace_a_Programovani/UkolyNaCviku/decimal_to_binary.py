import itertools

def dec_to_binary(num, nobits):
    grid = list(itertools.product([0, 1], repeat=nobits))

    for comb in grid:
        comb_rev = comb[::-1]
        res = []
        for i in range(len(comb_rev)):
            res.append(comb_rev[i]*(2**i))

        sum_res = sum(res)
        if sum_res == num:
            break
    if sum_res == num:
        print(f"{num} can be written as {nobits}-bits as follows: {comb}")
    else:
        print(f"{num} cannot be written as {nobits}-bits")


numbers = [4,18,15,255,1023,2047,42,118]
for number in numbers:
    dec_to_binary(number, 4)
    dec_to_binary(number, 8)