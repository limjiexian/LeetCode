from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        """DFS brute force"""
        # def dfs(i, total):
        #     # base case 
        #     if i > n-1:
        #         return total

        #     # rob current hse
        #     a = dfs(i+2, total + newNum[i])

        #     # dont rob current hse
        #     b = dfs(i+1, total)

        #     return max(a, b)
        
        # # rob first house, -> remove 4 from the nums list
        # newNum = nums[:len(nums)-1]
        # n = len(newNum)
        # amt_one = dfs(0, 0)
        
        
        # newNum = nums[1:]
        # n = len(newNum)
        # amt_two = dfs(0, 0)

        # return max(amt_one, amt_two)

        """DFS with cache"""
        # if len(nums) == 1:
        #     return nums[0]

        # def dfs(i):
        #     # base case
        #     if i >= len(newNums):
        #         return 0

        #     if memo[i] != -1:
        #         return memo[i]

        #     memo[i] = max((dfs(i+2) + newNums[i]), dfs(i+1))

        #     return memo[i]

        # n = len(nums)
        # newNums = nums[:n-1]
        # memo = {i: -1 for i in range(len(newNums))}
        # a = dfs(0)

        # newNums = nums[1:]
        # memo = {i: -1 for i in range(len(newNums))}
        # b = dfs(0)

        # return max(a, b)

        """Iterative Bottom up"""
        # if len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return max(nums[0], nums[1])

        # dp_one = [0] * (len(nums)-1)     # -1 to the len cos we rob first house and then remove last house
        # dp_two = [0] * (len(nums)-1)     # -1 to the len cos we skip first house and rob last house

        # nums_one = nums[:len(nums)-1]
        # nums_two = nums[1:]

        # # set 1
        # dp_one[0] = nums_one[0]
        # dp_one[1] = max(nums_one[1], dp_one[0])

        # for i in range(2, len(nums_one)):
        #     dp_one[i] = max(dp_one[i-2] + nums_one[i], dp_one[i-1])
        
        # # set 2
        # dp_two[0] = nums_two[0]
        # dp_two[1] = max(nums_two[1], dp_two[0])

        # for i in range(2, len(nums_two)):
        #     dp_two[i] = max(dp_two[i-2] + nums_two[i], dp_two[i-1])

        # return max(dp_one[-1], dp_two[-1])


        """Two pointer DP"""

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        newNums = nums[:len(nums)-1]
        
        back, front = newNums[0], max(newNums[0], newNums[1])

        for i in range(2, len(newNums)):
            current = max(back + newNums[i], front)
            temp = front
            front = current
            back = temp

        a = front

        newNums = nums[1:]
        back, front = newNums[0], max(newNums[0], newNums[1])

        for i in range(2, len(newNums)):
            current = max(back + newNums[i], front)
            temp = front
            front = current
            back = temp

        b = front

        return max(a, b)


# 9/12/2024 ver

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """ Brute Force """
        # def dfs(i, total, sub_nums):
        #     if i >= len(sub_nums):
        #         return total
            
        #     # dont rob current
        #     a = dfs(i+1, total, sub_nums)

        #     # rob current
        #     b = dfs(i+2, total, sub_nums) + sub_nums[i]
        
        #     return max(a, b)

        # return max(dfs(0, 0, nums[0:len(nums)-1]), dfs(0, 0, nums[1:]))

        """ Cache """
        # memo = {}

        # if len(nums) == 1:
        #     return nums[0]

        # def dfs(i, sub_nums):
        #     if i >= len(sub_nums):
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     # print("in i", i)
        #     a = dfs(i+1, sub_nums)

        #     b = dfs(i+2, sub_nums) + sub_nums[i]

        #     memo[i] = max(a, b)

        #     # print("exit i", i)
        #     return memo[i]
        
        # dfs(0, nums[0:len(nums)-1])
        # set_one = memo[0]

        # memo = {}
        # dfs(0, nums[1:])
        # set_two = memo[0]

        # return max(set_one, set_two)

        """ Iterative Bottom Up """
        # sub_nums = nums[0:len(nums)-1]
        # dp = [0] * (len(sub_nums) + 2)

        # for i in range(len(sub_nums)-1, -1, -1):
        #     dp[i] = max(dp[i+1], dp[i+2] + sub_nums[i])
        
        # set_one = dp[0]

        # dp = [0] * (len(sub_nums) + 2)
        # sub_nums = nums[1:]

        # for i in range(len(sub_nums)-1, -1, -1):
        #     dp[i] = max(dp[i+1], dp[i+2] + sub_nums[i])

        # set_two = dp[0]

        # return max(set_one, set_two)

        """ Two Pointer """

        # if len(nums) == 1:
        #     return nums[0]

        # nums_one = nums[0:len(nums)-1]
        # nums_two = nums[1:]

        # f1, b1, f2, b2 = 0, 0, 0, 0

        # for i in range(len(nums_one)-1, -1, -1):
        #     c1 = max(f1, b1 + nums_one[i])
        #     c2 = max(f2, b2 + nums_two[i])

        #     f1, b1 = c1, f1
        #     f2, b2 = c2, f2
        
        # return max(f1, f2)

















