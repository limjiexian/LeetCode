from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        # Initialize the queue with all rotten oranges and count fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                
        def rot(r, c) -> bool:
            # Ensure the cell is within bounds and contains a fresh orange
            if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1:
                grid[r][c] = 2  # Mark as rotten
                q.append((r, c))  # Add to the queue
                return True
            return False

        timer = 0
        while q:
            qSize = len(q)
            newlyRotten = False

            while qSize > 0:
                qSize -= 1
                r, c = q.popleft()

                # this will lead to short-circuit, if first rot function return true, the rest of the rot function
                # wont be called
                # if rot(r + 1, c) or rot(r - 1, c) or rot(r, c + 1) or rot(r, c - 1):
                #     newlyRotten = True

                if rot(r + 1, c): newlyRotten = True
                if rot(r - 1, c): newlyRotten = True
                if rot(r, c + 1): newlyRotten = True
                if rot(r, c - 1): newlyRotten = True

            if newlyRotten == True:
                timer +=1 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return timer
