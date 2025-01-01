from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """ Brute Force O(n^3) """
        # nums.sort()  # Sort the array to handle duplicates easily
        # res = []

        # for i in range(len(nums)):
        #     # Skip duplicate elements for 'i'
        #     if i != 0 and nums[i-1] == nums[i]:
        #         continue

        #     for j in range(i+1, len(nums)):
        #         # Skip duplicate elements for 'j'
        #         if j != i+1 and nums[j-1] == nums[j]:
        #             continue

        #         for k in range(j+1, len(nums)):
        #             # Skip duplicate elements for 'k'
        #             if k != j+1 and nums[k-1] == nums[k]:
        #                 continue

        #             # Check if the triplet sums to zero
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.append([nums[i], nums[j], nums[k]])

        # return res

        """ Brute Force Better Solution O(n^3) """
        # res = set()
        # nums.sort()

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 res.add(tuple([nums[i], nums[j], nums[k]]))

        # return [list(i) for i in res]

        """ Two Pointer """
        # [-1, 0, 1, 2, -1, -4]
        # [-4, -1, -1, 0, 1, 2]
        nums.sort()
        res = []

        for i in range(len(nums)):
             # Skip duplicates for 'i'
            if i != 0 and nums[i-1] == nums[i]:
                continue

            l, r = i + 1, len(nums)-1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                if three_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # if found sol alr, we move l and r to see if other combi can be our sol 
                    l += 1
                    r -= 1
                    
                    # skip duplicates for l
                    # we dont need do for r -> because -> look at notes
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
                
        return res
            

        


















        





