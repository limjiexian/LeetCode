from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Given 
        # - an array of integers candidates (got duplicates)
        # - target integer target

        # Goal
        # - return a list of all unique combinations of candidates that sum to target

        candidates.sort()
        
        n = len(candidates)
        res, sol = [], []

        def backtrack(i, total):
            
            # base case
            if total == target:
                res.append(sol[:])
                return

            if total > target or i >= n:
                return
            
            sol.append(candidates[i])
            backtrack(i+1, total+candidates[i])
            sol.pop()

            # basically if you already used the element previously, there is no point considering them again as you will simply get the same result
            while i+1 <= n-1 and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, total)

        backtrack(0, 0)

        return res