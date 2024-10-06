from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # An array of distinct integers nums
        # target integer target
        # Goal:
        # - return all possible combinations of nums where the chosen numbers sum to target

        res = []
        combi = []

        def dfs(i, total):
            # base case: if the current combination sums up to the target
            if total == target:
                res.append(combi.copy())  # append a copy of the current combination to the result
                return

            # if we have exceeded the bounds of the nums array or the total exceeds the target, we stop
            if i > len(nums) - 1 or total > target:
                return

            # include the current element nums[i] in the combination
            combi.append(nums[i])
            # we allow repeated elements by passing `i` (not `i + 1`) to allow the same element to be considered again
            dfs(i, total + nums[i])

            # backtrack by removing the last added element before considering the next element
            combi.pop()
            # explore the next element in the array (move to the next index)
            dfs(i + 1, total)

        dfs(0, 0)  # start the depth-first search from the first element with a total sum of 0
        return res
