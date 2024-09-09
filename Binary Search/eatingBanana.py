import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # integer array piles, piles[i] contains # of bananas in that ith pile
        # integer h - # of hours u need to eat all bananas
        # k = eating rate of bananas per hour
        # each hour you choose a pile and eat k banana from it
        # if pile has less than k bananas, you can finish eating the pile but you cant use the spare time to eat another pile
        # return min integer k such that you can eat all the bananas within h hours

        smol, large = 0, max(piles)
        smallestK = float('inf')

        one = 0

        while smol <= large:
            k = (smol + large) // 2
            k = max(1, k)

            time = 0
            for pile in piles:
                one = math.ceil(pile / k)
                time += one

            if time < h:
                large = k - 1
                smallestK = min(smallestK, k)
            elif time > h:
                smol = k + 1
                
            else:
                large = k - 1
                smallestK = min(smallestK, k)                

        return smallestK

piles=[1,4,3,2]
h=9

sol = Solution()
output = sol.minEatingSpeed(piles, h)
