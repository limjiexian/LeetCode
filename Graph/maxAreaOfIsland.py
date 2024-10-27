from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Given
        # - grid, 0 == water, 1 == land
        # island == connected 1
        # Task
        # - return max area of an island in grid
        # - area = # of cells within the island aka # of 1

        visited = set()
        maxArea = 0
        
        def backtrack(x, y):
            # base case
            # check boundaries first
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return 0

            if (x,y) in visited or grid[x][y] == 0:
                return 0

            visited.add((x,y))
            area = 1

            # main
            # check 4 directions
            area += backtrack(x,y-1) # left 
            area += backtrack(x,y+1) # right
            area += backtrack(x-1,y) # top
            area += backtrack(x+1,y) # bot

            return area
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    maxArea = max(maxArea, backtrack(i, j))


        return maxArea
