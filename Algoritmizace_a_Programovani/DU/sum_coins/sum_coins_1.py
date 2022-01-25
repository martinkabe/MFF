
def read_inputs():
    n_coins = int(input())
    if n_coins < 1 or n_coins > 20:
        return None
    coins = list(map(int, input().split()))
    if len(coins) != n_coins:
        return None
    sum_coins = int(input())
    if sum_coins < 0:
        return None
    return n_coins, coins, sum_coins


def coinCombinations(coins, amount, indx, lst):
    if amount == 0:
        print(*lst)
        return
    
    if amount < 0:
        return
    
    for i in range(indx, len(coins)):
        coin = coins[i]
        if amount >= coin:
            lst.append(coin)
            coinCombinations(coins, amount-coin, i, lst)
            lst.pop()


if __name__=="__main__":
    inpt = read_inputs()
    if inpt is not None:
        n_coins, coins, sum_coins = inpt
        # coins.sort()
        coinCombinations(coins, sum_coins, 0, list())

# input:
# 3
# 5 2 1
# 9

# output:
# 5 2 2
# 5 2 1 1
# 5 1 1 1 1
# 2 2 2 2 1
# 2 2 2 1 1 1
# 2 2 1 1 1 1 1
# 2 1 1 1 1 1 1 1
# 1 1 1 1 1 1 1 1 1