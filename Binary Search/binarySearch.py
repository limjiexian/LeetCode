from typing import List 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # array of distinct integers nums
        # sorted in increasing order
        # u got a target int
        # goal search for target within nums, return its index, otherwise return -1
        # sol must be O(logn)

        #          0 1 2 3 4 5
        # nums = [-1,0,2,4,6,8], target = 4, mid = 2
        # start = 0, end = 5
        # mid = 5 // 2 = 2
        # nums[2] = 2

        # if target=4 > nums[2]=2 // means we need take right side array

        # [4, 6, 8], mid = 6
        # [4]

        l = 0
        r = len(nums) - 1
                
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m -1
            else:
                l = m + 1
            
        return -1
                

            
sol = Solution()
nums=[-1,0,2,4,6,8]
target=3
output = sol.search(nums, target)