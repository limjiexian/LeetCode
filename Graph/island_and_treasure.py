class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Given:
        - 2D grid:
           -1  = water cell
            0  = treasure
           inf = traversable land cell  // = 2147483647

        Task:
        - fill each land cell with the dist to its nearest treasure chest
        - if a land cell cant reach a treasure chest -> value shld remain inf


        Input: [
                    [t, x, 0, t],
                    [t, t, t, x],
                    [t, x, t, x],
                    [0, x, t, t]
                ]

        """

        def add_cells(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or grid[r][c] == -1:
                return False
            
            q.append((r, c))
            visited.add((r, c))

        q = deque()
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    add_cells(r, c)
                
        timer = 0
        while q:
            size = len(q)

            while size != 0:   
                r, c = q.popleft()

                grid[r][c] = timer

                # check for directions that we can spread to
                add_cells(r+1, c)
                add_cells(r-1, c)
                add_cells(r, c+1)
                add_cells(r, c-1)
                
                size -= 1
                
            timer += 1  



# [[9,-1,0,3],
#  [7,6,2,-1],
#  [4,-1,5,-1],
#  [1,-1,8,10]]

# Output: [
#  [3,-1,0,1],
#  [2,2,1,-1],
#  [1,-1,2,-1],
#  [0,-1,3,4]
# ]






