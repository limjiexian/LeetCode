class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        """ Brute Force """
        # total = 0
        # for num in nums:
        #     total += num
        
        # if total % 2 != 0:
        #     return False

        # half = total / 2
        
        # def dfs(i, total):
        #     # base case
        #     if total == half:
        #         return True
            
        #     if total < half:
        #         return False
            
        #     if i >= len(nums):
        #         return False
            
        #     # include
        #     include = dfs(i+1, total - nums[i])
        
        #     # exclude
        #     exclude = dfs(i+1, total)

        #     return include or exclude 
        
        # return dfs(0, total)

        """ With Cache """
        # total = 0
        # for num in nums:
        #     total += num
        
        # if total % 2 != 0:
        #     return False

        # half = total / 2

        # memo = {i: {} for i in range(len(nums))}

        # def dfs(i, total):
        #     if i >= len(nums):
        #         return False

        #     if total in memo[i]:
        #         return memo[i][total]

        #     if total == half:
        #         return True

        #     if total < half:
        #         return False

        #     # include
        #     include = dfs(i+1, total - nums[i])
        
        #     # exclude
        #     exclude = dfs(i+1, total)

        #     memo[i][total] = include or exclude

        #     return memo[i][total]

        # dfs(0, total)

        # return memo[0][total]

        """ Iterative Bottom up """
        total = sum(nums)
        
        # If the total sum is odd, it's impossible to partition it into two equal parts
        if total % 2 != 0:
            return False

        half = total // 2
        
        # Initialize DP array with False values
        # dp[x] = True means we can achieve a sum of x using some combination of numbers in nums.
        dp = [False] * (half + 1)
        
        # Base case: we can always achieve a sum of 0
        dp[0] = True
        
        # Iterate through each number in the list
        for num in nums:
            # Update the DP table from back to front to avoid overwriting values
            for j in range(half, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        # The answer is whether we can achieve a sum of half
        return dp[half]

















                

