

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """ Binary Search """

        # [1, 4, 3, 2] h = 9

        # eating rate 1/hr
        # eating rate 4/hr

        # perform binary search, then say e.g. we get 2/hr, then we check did we managed to eat finish within h hours, if we never we go right sub else left
        
        r = max(piles)
        l = 1

        min_k = float("inf")
    
        while l <= r:
            m = (l+r) // 2

            # perform our calculation to check if m/hr is valid
            time = 0
            for pile in piles:
                time += math.ceil(pile/m)
            
            print("m =", m)
            print("time = ", time)

            if time <= h:    # go left to find slower eat rate that is still valid
                min_k = min(min_k, m)
                print("min_k ", min_k)
                r = m - 1
            elif time > h:  # go right cos current eat rate is too slow
                l = m + 1
        
        return min_k


# 1//2 = 1
# 4//2 = 2
# 3//2 = 2
# 2//2 = 1




