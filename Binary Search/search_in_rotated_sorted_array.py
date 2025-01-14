from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            
            # as we will traverse left or right array depending on whether target is < or > but we dont include ==, therefore we need this if statement
            # to check nums[m] == target
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]:      # m belongs to left sorted portion
                # there are two situation whereby target dont belong to left portion array
                # 3,4,5
                # case 1 -> target less than 3
                # case 2 -> target more than 5
                if target < nums[l] or target > nums[m]:    # search right
                    l = m + 1
                else:
                    r = m - 1
            else:                       # m belongs to right sorted portion
                # similar to the one in if statement
                if target < nums[m] or target > nums[r]:    # search left
                    r = m - 1
                else:
                    l = m + 1

        return -1

