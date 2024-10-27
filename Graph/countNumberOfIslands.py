from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 2D Grid
        # - 1 == Land
        # - 0 == Water
        # Task
        # - Count and return the number of island
        # - Island == have connecting land and this is surrounded completely by water

        # idea
        # once we found our first 1, add it into our visited island, 
        # we backtrack and check its surrounding, keep adding 1 until we cant reach any other 1
        # then we loop next index, if is visited alr means we already counted it as our island we just
        # go next
        
        island = set()
        count = 0

        def backtrack(x, y):
            # base case            
            # boundaries
            if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
                return

            if (x,y) in island or grid[x][y] == '0':
                return

            # main code
            
            island.add((x,y))

            # check surrounding
            backtrack(x-1, y) # top
            backtrack(x+1, y) # bot
            backtrack(x, y-1) # left
            backtrack(x, y+1) # right

            return

        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == "1" and (i,j) not in island:
                    count += 1
                    backtrack(i, j)

        return count


