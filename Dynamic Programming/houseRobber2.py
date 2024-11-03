from typing import List


# Jx method
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # houses arranged in a circle
#         # first and last house are neighbors

#         # When the problem has a circular constraint (like the first and last house being neighbors), 
#         # it’s essential to treat each case independently.

#         two, one = 0, 0
#         size = len(nums)
#         rob = True
#         # [two, one, 0, 1, 2, n]

#         for i in range(size):
#             if i == size-1:
#                 continue

#             if rob == True:
#                 amt = two + nums[i]
#                 rob = False
#             else: 
#                 amt = max(one, two + nums[i])

#             two = one
#             one = amt
        
#         maxOne = one

#         two, one = 0, 0
        
#         # [two, one, 0, 1, 2, n]
#         for i in range(size):
#             if rob == False:
#                 amt = one
#                 rob = True
#             else: 
#                 amt = max(one, two + nums[i])

#             two = one
#             one = amt
        
#         return max(maxOne, one)


# neetcode method

class Solution:
    
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), 
                            self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            newRob = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2

