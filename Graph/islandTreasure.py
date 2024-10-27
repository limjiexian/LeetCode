from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Given
        # m x n 2D grid
        # -1 = water cell (CANNNOT TRAVERSE)
        # 0 = treasure chest
        # INF = A traversable land cell

        # Task
        # set each land cell with the dist to its nearest treasure chest
        # if land cell cannot reach any treasure chest -> let it remain INF

        # Thought process
        # for each INF we recurrsively see if we can traverse to treasure chest
        # each recursion, we return if we cant progress anymore or if we reached the treasure chest
        # as we progress on each step, we increase count +=1, if we reach treasure chest we will return
        # the final count value

        # for the 4 direction path, we get the smallest count value and save to the INF

        visited = set()

        def addCell(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == -1 or (x,y) in visited:
                return
            visited.add((x,y))
            q.append((x,y))

        q = deque()

        # append all the treasure chest location to our queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))

        dist = 0

        while q:
            for k in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist

                addCell(i-1, j)
                addCell(i+1, j)
                addCell(i, j-1)
                addCell(i, j+1)

            dist += 1

# Time complexity
# - each cell is processed at most once so -> O(m * n)

# Space complexity
# - visited set store m * n nodes -> O(m * n)




                




            
            