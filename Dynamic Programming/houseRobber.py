from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[i] -> how much money ith hse have
        # house arranged in a straight line
        # cannot rob 2 adjacent houses

        # If one > two + nums[i]: It means the maximum amount robbed so far (by skipping the current i house) 
        # is greater than what you’d get by robbing the current house. 
        # So, you skip robbing this house and keep one as the maximum.

        # If two + nums[i] >= one: It means robbing the current house (by adding nums[i] to two) would 
        # give you a higher amount than skipping it. So, you choose to rob this house.


        two, one = 0, 0

        for i in range(0, len(nums)):
            amt = max(one, two + nums[i])
            two = one
            one = amt
        
        return one

        

            