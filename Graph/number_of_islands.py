from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given:
        - 2D grid
            - '1' = land
            - '0' = water

        Task:
        - count and return the # of islands

        Definition:
        - island -> formed by connecting adj lands horizontally or vertically and is surrounded by the water
        """

        visited = set()

        ROW, COL = len(grid), len(grid[0])

        def backtrack(row, col):
            # base case
            if row >= ROW or col >= COL or row < 0 or col < 0 or grid[row][col] != "1" or (row, col) in visited:
                return 

            # main code
            visited.add((row, col))
    
            backtrack(row+1, col)
            backtrack(row-1, col)
            backtrack(row, col+1)
            backtrack(row, col-1)

            return

        count = 0

        for r in range(ROW):
            for c in range(COL):
                if (r, c) not in visited and grid[r][c] == '1':
                    count += 1
                    backtrack(r, c)
        
        return count

