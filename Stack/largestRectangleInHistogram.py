class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pairs: start, height

        for i, h in enumerate(heights):
            start = i # cos we dont know if we can extend it backwards or extend it to the left <<<
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                currArea = (i - index) * height
                maxArea = max(maxArea, currArea)
                # since we know this height was greater than the current height we are visiting
                # it means we can extend our current height to the start index backwards to the index we just popped
                start = index

            stack.append((start, h))

        while stack:
            index, height = stack.pop()
            currArea = (len(heights) - index) * height
            maxArea = max(maxArea, currArea)

        return maxArea
