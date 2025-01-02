from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []  # pair: temp, index
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            # maintain our monotonic increasing stack
            while stack and t > stack[-1][0]:
                # if we pop means we found a future day that has high temperate than item
                item = stack.pop()
                res[item[1]] = i - item[1]

            stack.append([t, i])

        return res
        