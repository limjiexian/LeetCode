from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # given unsorted array of integers nums
        # return the length of the longest consecutive elements sequence
        
        
        # what does longest consecutive elements sequence mean?
        # means like e.g. 1,2,3,4 means longest length will be = 4, 
        
        # Attempt thought process
        # probably need to sort the array?
        # then traverse through the sorted array, count consecutive elements
        # but sort algorithm usually takes o(nlogn), this question wants us to do it in O(n) time

        # store them into hash set?
        # we only want to look at element that have no element - 1
        # because that will mean that this element is the start of a sequence
        # if it has element -1 means -> it is like in the middle of a sequence so we just ignore
        # once we found our element -1, then we start counting element + 1 (if it exist)

        numSet = set(nums)
        longest = 0 
        length = 0
        for num in nums:
            if (num - 1) not in numSet:
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
                length = 0

        return longest 
        
sol = Solution()

nums = [100,4,200,1,3,2]

output = sol.longestConsecutive(nums)

print(output)