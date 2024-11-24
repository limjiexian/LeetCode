from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Given: 
        # - an integer array nums
        
        # Goal:
        # - return the length of the longest strictly increasing subsequence
        
        """
        Thought process:
        
        i am thinking, we can traverse the list, and then for each number check if it is larger than or equal nums[i+1]. If larger, we remove that element?

        [9, 1, 4, 2, 3, 3, 7]
        [1, 2, 3, 7]


        [0, 3, 1, 3, 2, 3]
        [0, 1, 2, 3]

        seems like it works so far ok lets try implement this with backtracking. 
        hmm actually nvm, think just use a for loop do can already, dont need backtracking LOL
        
        additional condition -> not only that the num[i] must be <= nums[i+1], it must also be smaller than the numbers that came before it
        """
        count = 0 
        minNum = float("inf")

        for i in range(len(nums)):
            if i+1 > len(nums)-1:
                break
            
            # check if nums[i] is smaller than nums[i+1]
            if nums[i] < nums[i+1]:
                # if smaller, check if nums[i] is smaller than elements that came before it
                if nums[i] >= minNum:
                    count += 1
                    minNum = float('inf')
                
                minNum = min(minNum, nums[i])
            else:
                count += 1

        
        size = len(nums)
        output = size - count

        return output


s = Solution()

s.lengthOfLIS(nums=[9,1,4,2,3,3,7])