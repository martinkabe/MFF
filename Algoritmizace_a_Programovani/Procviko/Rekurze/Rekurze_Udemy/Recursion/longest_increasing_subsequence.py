# https://www.youtube.com/watch?v=cjWnW0hdF1Y

from typing import List

def lengthOfLIS(nums: List[int]) -> int: # O(n^2)
    LIS = [1] * len(nums)

    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            print(f"Comparing {nums[i]} and {nums[j]}")
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])
                print(*LIS)
    return max(LIS)


arr = [0,1,0,3,2,3]
print(lengthOfLIS(arr))
