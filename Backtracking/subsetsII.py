
from typing import List

""" 
MY INITIAL METHOD:
Think the problem with this method, not that efficient because my base case "if sol not in res" is will keep do O(n) time to scan whether sol is in res. 
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Given an array nums of integers (may contain dupes)
        # Goal:
        # - return all possible subsets
        # - sol must not contain duplicate subsets

        # subset
        # -> a subset of a set is any combination of elements where ORDER DOES NOT MATTER
        # -> we dont care about the order of the elements in a subset. e.g. [1,2,3] same as [1,3,2]

        # our array may have duplicates
        # so how do we solve knowing this?

        n = len(nums)
        res, sol = [], []

        nums.sort()

        def backtrack(i):

            # base case
            if n == i:
                if sol not in res:
                    res.append(sol[:])
                return
        
            # include nums[i]
            sol.append(nums[i])
            backtrack(i+1)

            # exclude nums[i]
            sol.pop()
            backtrack(i+1)

        backtrack(0)

        return res

        # time complexity:
        # O(2^n * n)

        # space complexity:
        # res size O(2^n * n) + depth of tree O(n) 


"""
Neetcode Ver

"""

