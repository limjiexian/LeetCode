from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ Iterative Binary Search """
        l, r = 0, len(nums)-1
        
        while l <= r:
            m = (r+l) // 2
            # if interview ask what if we have integer overflow from adding r + 1?
            # use m = l + (r-l) // 2
            # because r-l // 2 -> == half the distance. so l + half distance will then give us the mid point

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        

        # 0, 1, 2, 3, 4

        # l           r

        # 4 - 0  // 2 = 2

        # 4 - 2 // 2 = 1
