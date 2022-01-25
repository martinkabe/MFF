from typing import List

def combs(nums: List):
    if len(nums) == 0:
        return [[]]
    
    combins = []
    for comb in combs(nums[1:]):
        combins += [comb, comb + [nums[0]]]
    
    return combins

print(combs([1,2,3]))

