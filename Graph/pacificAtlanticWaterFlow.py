from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # heights[r][c] == height above sea level of the cell at coordinate (r,c)
        # water can flow to neighboring cell ONLY IF their height is equal or lower
        # Top and Left side -> Pacific Ocean
        # Bot and Right side -> Atlantic Ocean
        # water can flow from cell into both ocean

        # Task
        # find all cells whereby water can flow from the cell to both the pacific and atlantic ocean
        # return it as 2D list [[r,c]]

        ROWS, COLS = len(heights), len(heights[0])
    
        res = []
        pac, atl = set(), set()

        def backtrack(r, c, visited, prevHeight):
            # base case
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited  or heights[r][c] < prevHeight:
                return
            
            visited.add((r,c))
            
            backtrack(r-1, c, visited, heights[r][c])
            backtrack(r+1, c, visited, heights[r][c])
            backtrack(r, c-1, visited, heights[r][c])
            backtrack(r, c+1, visited, heights[r][c])

        for c in range(COLS):
            backtrack(0, c, pac, heights[0][c])
            backtrack(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            backtrack(r, 0, pac, heights[r][0])
            backtrack(r, COLS-1, atl, heights[r][COLS-1])
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res
        
        # time complexity O(m*n)
        # For each ocean, you initiate a DFS from its boundary cells, which might traverse all reachable cells.
        # Since each cell can potentially be visited once during the Pacific DFS and once during the Atlantic DFS, this results in 2 * (m * n) total cell visits.
        # approximate to O(m*n)

        # Space Complexity
        # Visited Sets (pac and atl):
        # Each of these sets can store up to m * n cells in the worst case, so together they require O(m * n) space.
        # Recursive Call Stack:
        # In the worst case, the recursion depth could go up to m * n if you have to traverse a single long path without 
        # returning, which requires O(m * n) space for the call stack.