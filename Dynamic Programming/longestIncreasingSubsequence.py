from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """ dfs brute force """
        # def dfs(i, j):
        #     # base case
        #     if i >= len(nums):
        #         return 0 # no more choices so return 0

        #     # exclude
        #     LIS = dfs(i+1, j)

        #     # include
        #     if j == -1 or nums[j] < nums[i]:
        #         LIS = max(LIS, dfs(i+1, i) + 1)   # cos we include so add 1
            
        #     return LIS
        
        # return dfs(0, -1)

        """ with cache """
        # memo = {i: {} for i in range(len(nums))}

        # def dfs(i, j):
        #     if i >= len(nums):
        #         return 0
            
        #     if j in memo[i]:
        #         return memo[i][j]

        #     # exclude
        #     LIS = dfs(i+1, j)

        #     # include
        #     if j == -1 or nums[i] > nums[j]:
        #         LIS = max(LIS, dfs(i+1, i) + 1)

        #     memo[i][j] = LIS

        #     return memo[i][j]

        # dfs(0, -1)

        # return memo[0][-1]

        """ iterative bottom up """
        # cos if we dont include current cos of future, by default we should have LIS 1 for this nums[i] element
        dp = {i: 1 for i in range(len(nums))}

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                # include
                # +1 is for including current nums[i]
                # dp[j] is to get the future LIS
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) # left -> dp[i] is basically our exclude and our default 1 value 

        return max(dp.values())





