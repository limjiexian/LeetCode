from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Given:
        - an array of integers candidate (contain dupes)
        - a target integer

        Task:
        - Return list of all unique combi of candidates that sum up to target (this will be our base case)

        Conditions:
        - Can only select each element once.

        [1, 2, 3, 4, 5]


        """

        candidates.sort()

        res, sol = [], []

        def dfs(i, total):
            # base case
            if total == target:
                res.append(sol[:])
                return
            
            if total > target or i >= len(candidates):
                print("LOL", sol)
                return

            # include
            sol.append(candidates[i])
            # print(sol)
            dfs(i+1, total + candidates[i])

            # exclude
            sol.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total + candidates[i])

        dfs(0, 0)

        return res

s = Solution()

s.combinationSum2(candidates=[1,2,3,4,5], target=7)