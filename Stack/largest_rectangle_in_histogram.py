from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # The key idea is that for each bar in the histogram:

        # Height is fixed: The rectangle's height is determined by the height of the current bar.
        # Width can vary: To maximize the rectangle's area, we expand the rectangle left and right until we hit a bar shorter than the current bar.
        # Calculate the area: The width of the rectangle is the range of bars that are at least as tall as the current bar. The area is then:
        # Area = Height of current bar * Width of rectangle
        # Iterate for all bars: We do this for every bar and keep track of the largest area found.

        """ Brute Force O(n^2)"""
        # max_area = float("-inf")

        # for i in range(len(heights)):
        #     h = heights[i]

        #     left_most = i
        #     while left_most >= 0 and heights[left_most] >= h:
        #         left_most -= 1
            
        #     # At this point, leftMost points to the first invalid index that is outside the valid rectangle.
        #     # To get back to the last valid index inside the rectangle, you need to adjust:
        #     left_most += 1


        #     # Starts at `i + 1` because the current bar is already part of the rectangle by default.
        #     #   - can just start at right_most = i
        #     #   - if it confuses you
        #     right_most = i + 1
        #     while right_most < len(heights) and heights[right_most] >= h:
        #         right_most += 1

        #     # At this point, rightMost points to the first invalid index that is outside the valid rectangle.
        #     # To get back to the last valid index inside the rectangle, you need to adjust:
        #     right_most -= 1

        #     area = (right_most - left_most + 1) * heights[i]
        #     max_area = max(max_area, area)

        # return max_area

        """ Optimised Using Monotonic Stack (increasing) """

        # increasing stack cos, if there is a height lower than existing one in the stack, means it cant be extended anymore
        # so we pop and process it

        stack = []  # pair: index, height
        max_area = 0 

        for i, h in enumerate(heights):
            # cos we dk if we can extend to the left yet
            start = i

            while stack and h < stack[-1][1]:
                old_i, old_h = stack.pop()

                width = i - old_i
                area = old_h * width
                max_area = max(max_area, area)

                # Update the start to extend the current bar to the left
                #   - cos if curr bar height < old bar height
                #   - means curr bar can extend to the left, until the old bar
                start = old_i

            stack.append([start, h])
        
        # means they can extend all the way to the right
        r = len(heights)
        for l, h in stack:
            width = r - l
            area = h * width
            max_area = max(max_area, area)

        return max_area



















