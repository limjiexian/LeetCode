from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """ Brute Force """
        # max_area = float('-inf')

        # # base * height
        # # base -> j - i
        # # height -> min(height1, height2)

        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         h1 = heights[i]
        #         h2 = heights[j]

        #         area = (j-i) * (min(h1,h2))

        #         max_area = max(max_area, area)
        
        # return max_area

        """ Two Pointer """
        l, r = 0, len(heights)-1

        max_area = float('-inf')
        while l < r:
            h1 = heights[l]
            h2 = heights[r]

            area = (r-l) * (min(h1,h2))
            max_area = max(max_area, area)

            if h1 < h2:
                l += 1
            else:
                r -= 1
            
        return max_area


