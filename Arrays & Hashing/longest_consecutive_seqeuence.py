from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ Brute Force"""
        # res = 0
        # store = set(nums)

        # for num in nums:
        #     streak, curr = 0, num

        #     while curr in store:
        #         curr += 1
        #         streak += 1

        #     res = max(res, streak)

        # return res          

        """ Sorting """
        # if not nums:
        #     return 0

        # res = 0
        # nums.sort()
        
        # i = 0
        # curr = nums[i]
        # streak = 0

        # while i < len(nums):
        #     if curr != nums[i]:
        #         curr = nums[i]
        #         streak = 0
            
        #     while i < len(nums) and curr == nums[i]:
        #         i += 1
            
        #     streak += 1
        #     curr += 1

        #     res = max(res, streak)

        # return res


        """ Hash set """

        # 2345 1020

        # start of the subsequence will have no digit on its left and have a digit on its right
        # end of the subsequence will have digit on its left and no digit on its right
        #     - actually this dont really matter, we just need identify the start then just count +=1 and then traverse down.
        #     - if reach the end, we just check with max count then go find our next start digit

        res = 0
        store = set(nums)

        for num in nums:
            left = num -1
            if left in store:
                continue
            
            curr = num
            streak = 0
            while curr in store:
                streak += 1
                curr += 1
            
            res = max(res, streak)
        
        return res



        """ my own Sorting ver that is more intuitive """
        # nums.sort()
        # max_streak = 0
        # i = 0
         
        # while i < len(nums):
        #     streak = 0
        #     curr = nums[i] 

        #     while i < len(nums) and curr == nums[i]:
        #         streak += 1
        #         curr += 1
        #         i += 1

        #         while i < len(nums) and nums[i] == nums[i-1]:
        #             i += 1
            
        #     max_streak = max(max_streak, streak)
            
        # return max_streak