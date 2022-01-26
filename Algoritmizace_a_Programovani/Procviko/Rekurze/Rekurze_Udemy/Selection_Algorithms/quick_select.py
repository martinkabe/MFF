import random
from typing import List

class QuickSelect:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.first_index = 0
        self.last_index = len(nums) - 1
    
    def run(self, k):
        return self.select(self.first_index, self.last_index, k-1)

    def select(self, first_index, last_index, k):

        pivot_index = self.partition(first_index, last_index)

        if pivot_index > k:
            return self.select(first_index, pivot_index - 1, k)
        elif pivot_index < k:
            return self.select(pivot_index + 1, last_index, k)
        
        return self.nums[pivot_index]


    def partition(self, index_first, index_last):
        pivot = random.randint(index_first, index_last)
        self.swap(pivot, index_last)

        for i in range(index_first, index_last):
            if self.nums[i] < self.nums[index_last]:
                self.swap(i, index_first)
                index_first += 1
        
        self.swap(index_first, index_last)

        return index_first
    
    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


arr = [1, 2, -5, 10, 100, -7, 3, 4]
qs = QuickSelect(arr)
result = qs.run(3)
print(result)