def sum_nat_nums(num: int) -> int:
    if num <= 1:
        return num
    return num + sum_nat_nums(num-1)

print(sum_nat_nums(5))