import math
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        minNum = float('inf')

        while l <= r:
            mid = (l+r) // 2

            # identify the sorted portion, get the min and eliminate it
            # means mid is in right sorted portion
            if nums[mid] <= nums[r]:
                minNum = min(minNum, nums[mid])
                r = mid - 1
            else: # means mid dont belong to the right portion, so we get the min of the left portion of the array that nums[mid] belongs to
                minNum = min(minNum, nums[l])
                l = mid + 1
                
        return minNum