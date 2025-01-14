from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        """ l < r version """
        # l, r = 0, len(nums)-1
        
        # while l < r:
        #     m = (l+r) // 2

        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m
        
        # return nums[l]

        """ l <= r version """
        # l, r = 0, len(nums)-1
        # res = float('inf')

        # while l <= r:
        #     m = (l+r) // 2

        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         res = min(res, nums[m])
        #         r = m - 1
        
        # return res

        # [3,4,5,[6],1,2]
    
        # [4,5,0,[1],2,3]

        # [1,2,3,[4],5,0,0]

        # [5,0,0]


        """ Neetcode Version """
        l, r = 0, len(nums)-1
        min_sol = float('inf')

        while l <= r:
            # case -> if we get to the point whereby the entire array is sorted aka no pivot 
            if nums[l] < nums[r]:
                min_sol = min(min_sol, nums[l])
                break

            m = (l + r) // 2
            min_sol = min(min_sol, nums[m])

            # m belongs to left sorted portion
            # take left min and go explore right 
            if nums[l] <= nums[m]:
                min_sol = min(min_sol, nums[l])
                l = m + 1
            else:
                r = m - 1
        
        return min_sol
                
























