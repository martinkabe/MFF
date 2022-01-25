# Longest increasing sequence

def lengthOfLIS(nums):
    N = len(nums)
    dp = [1]*N

    for n in range(N):
        for i in range(n):
            if nums[i] < nums[n]:
                dp[n] = max(dp[n], dp[i]+1)
    return max(dp)

arr = [10,3,1,6,2,2,7]
print(lengthOfLIS(arr))
