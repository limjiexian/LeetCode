from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0 = empty cell
        # 1 = fresh fruit
        # 2 = rotten fruit

        # if fresh fruit beside rotten fruit = fresh become rotten after 1min

        # return min # of minutes before all fresh fruit become rotten
        # if this doesnt happen return -1

        # Thought process
        # concurrent bfs from all the rotten fruits

        visited = set()
        q = deque()

        def corrupt(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or (x,y) in visited:
                return

            # because visiting again wont make sense if our bfs have already passed by this cell
            # i.e. the neighbouring cell have already been corrupted 
            visited.add((x,y))
            q.append((x,y))
        
        fresh = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    visited.add((i,j))
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        time = 0

        while q:
            newRotten = False

            for i in range(len(q)):
                x, y = q.popleft()

                # set food to rotten
                if grid[x][y] == 1:
                    newRotten = True
                    fresh -= 1
                    grid[x][y] = 2

                corrupt(x-1, y)
                corrupt(x+1, y)
                corrupt(x, y-1)
                corrupt(x, y+1)

            if newRotten == True:
                time += 1
        
        if fresh:
            return -1
        else:
            return time



