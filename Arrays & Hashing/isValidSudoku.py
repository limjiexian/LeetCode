from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  # key = (r /3, c /3)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                # i // 3, j // 3 is basically used to return us which subsquare box hash set of the 9x9 we want to check
                if (
                    board[i][j] in rows[i] 
                    or board[i][j] in cols[j] 
                    or board[i][j] in squares[(i//3, j//3)]
                    ):
                   return False
                else:
                    rows[i].add(board[i][j]) 
                    cols[j].add(board[i][j]) 
                    squares[(i//3, j//3)].add(board[i][j]) 
        
        return True
    
sol = Solution()
# board = [["1","2",".",".","3",".",".",".","."],
# ["4",".",".","5",".",".",".",".","."],
# [".","9","8",".",".",".",".",".","3"],
# ["5",".",".",".","6",".",".",".","4"],
# [".",".",".","8",".","3",".",".","5"],
# ["7",".",".",".","2",".",".",".","6"],
# [".",".",".",".",".",".","2",".","."],
# [".",".",".","4","1","9",".",".","8"],
# [".",".",".",".","8",".",".","7","9"]]

board = [["1","2",".",".","3",".",".",".","."],
         ["4",".",".","5",".",".",".",".","."],
         [".","9","1",".",".",".",".",".","3"],
         ["5",".",".",".","6",".",".",".","4"],
         [".",".",".","8",".","3",".",".","5"],
         ["7",".",".",".","2",".",".",".","6"],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".","4","1","9",".",".","8"],
         [".",".",".",".","8",".",".","7","9"]]

output = sol.isValidSudoku(board)

print(output)