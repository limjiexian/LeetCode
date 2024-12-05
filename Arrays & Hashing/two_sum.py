from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """ Brute Force -> O(n^2)"""
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        
        """ Hashmap Two pass-> O(n) """
        # seen = {}

        # # If there are duplicate values in nums, the first loop will overwrite the key in the `seen` dictionary
        # # with the index of the last occurrence of that value.
        # # However, in the second loop, as we traverse nums in order (from left to right),
        # # we will always process the first occurrence of a value first because we are iterating sequentially.
        # # This ensures that we never use the same index twice, as the condition `seen[diff] != index` 
        # # ensures the indices are distinct.
        # for index, num in enumerate(nums):
        #     seen[num] = index

        # for index, num in enumerate(nums):
        #     diff = target - num

        #     if diff in seen and seen[diff] != index:
        #         return [index, seen[diff]]

        """ Hashmap One pass-> O(n) """
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            print(seen.keys())
            
            if diff in seen:
                return [seen[diff], i]
            
            seen[num] = i


            