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

        """ Iterative Bottom Up Approach """

        dp = [1] * (len(nums))
        
        for i in range(len(nums)-1, -1, -1):
            # LIS at dp[i] stores the length of the longest increasing subsequence (LIS) starting at index i.
            # i.e. is the max of (selecting dp[i] itself only, select dp[i] and the LIS of dp[j])
            # say we have 1, 2, 4, 3
            # LIS of 3 will be 3 itself and i+1
            # LIS of 4 will be max(itself, itself and then select future aka LIS 3) == max(itself, 1 + LIS3)
            # LIS of 2 got 2 path, we either max(select itself, select itself and select future LIS 4) or max(select itself, select itself and skip LIS 3 and select future LIS 3)

            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)





