from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Given
        - nums, nums[i] == amt $ ith hse have
        - houses arranged in straight line

        Task
        - find the max $ u can rob without alerting the police(cannot rob 2 adjacent houses)
        
        """

        """ Brute Force """
        # def dfs(i, total):
        #     # base case
        #     if i > len(nums)-1:
        #         return total

        #     # rob current
        #     a = dfs(i+2, total + nums[i])

        #     # skip current
        #     b = dfs(i+1, total)

        #     return max(a, b)
        
        # return dfs(0, 0)

        """ With Cache """
        # memo = {i: -1 for i in range(len(nums))}

        # def dfs(i):
        #     # base case
        #     if i > len(nums)-1:
        #         return 0

        #     if memo[i] != -1:
        #         return memo[i]

        #     memo[i] = max((dfs(i+2) + nums[i]), dfs(i+1))

        #     return memo[i]
        
        # dfs(0)

        # return memo[0]

        """ Iterative Bottom up """
        # dp = [0] * (len(nums) + 2)
 
        # for i in range(len(nums)-1, -1, -1):
        #     dp[i] = max(dp[i+1], dp[i+2] + nums[i])
        
        # return dp[0]

        """ Two pointer"""

        # front, back = 0, 0 

        # for i in range(len(nums)-1, -1, -1):
        #     curr = max(front, back + nums[i])

        #     front, back = curr, front
        
        # return front






