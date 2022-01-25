# https://www.youtube.com/watch?v=H9bfqozjoqs
min_coins = 1000

def coinCombinations(coins, amount, indx, lst):
    global min_coins

    if amount == 0:
        if len(lst) < min_coins:
            min_coins = len(lst)
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

    return min_coins


if __name__=="__main__":
    coins = [1,3,4,5]
    sum_coins = 0
    min_coins = len(coins)
    result = coinCombinations(coins, sum_coins, 0, list())
    print(result)