from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 'X' and 'O' 2D board
        # border != surrounding 
        # if O is surrounded by X in the direction of left right up bottom, then we can convert O to X

        # Method
        # Reverse the question
        # Instead of finding the region that is surrounded, we find all the region that is not surrounded aka
        # 'O' that are at the border, and any other 'O' that is connected to them

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def backtrack(r, c):
            # base case
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visited or board[r][c] == "X":
                return
            
            visited.add((r,c))

            # backtrack to check for any O connected to this O
            backtrack(r-1, c)
            backtrack(r+1, c)
            backtrack(r, c-1)
            backtrack(r, c+1)
        
        # Traverse through the borders, to find any O
        # backtrack to find any O connected to these border O
        for c in range(COLS):
            backtrack(0, c)
            backtrack(ROWS-1, c)
        
        for r in range(ROWS):
            backtrack(r, 0)
            backtrack(r, COLS-1)
        
        # Change all region that we did not visit to X
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"
        
        return
        
        # Time complexity:
        # Worst case
        # each cell is being traversed at most once, as we only visit unmark O cells, say if all cells is O, then we will
        # visit all the cell in the board == rows * cols == O(m*n)
        # also at the end to flip O to X, we ran for r in and for c in, these two is already O(m*n)

        # Space complexity:
        # if whole board is O
        # - recursion depth is m*n 
        # - storage for visited set is also m*n
        # therefore ans = O(m*n)
        