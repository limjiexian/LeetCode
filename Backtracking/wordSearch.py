from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Given 2D grid;board and string;word
        # Goal:
        # - return true if word is present in the grid
        # - else return false 

        # For word to be present == you must be able to form it with a path in the board
        # with horizontally or vertically neighboring cells
        # Cell can only be used once
    
        # Idea
        # need to mark visited cells
        # traverse through the board, if got any cell that has same char as our first target char
        # mark cell visited, then check its surrounding, for each adjacent cell, we pass this cell into our backtracking
        # backtracking will return nothing if we cant find any target char
        # backtracking will return True if we managed to find the last target char

        # Row
        m = len(board)
        # Col
        n = len(board[0])

        visited = set()

        def backtrack(row, col, index):
            # base case
            if index == len(word):
                return True
            
            if (row, col) in visited:
                return False

            if row < 0 or col < 0 or row >= m or col >= n or board[row][col] != word[index]:
                return False

            visited.add((row, col))

            # check surrounding got char == word[index+1] char
            if (backtrack(row+1, col, index+1) or # down
                backtrack(row-1, col, index+1) or # up
                backtrack(row, col-1, index+1) or # left
                backtrack(row, col+1, index+1)): # right    
                return True
            
            visited.remove((row,col))

            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
            
        return False


        # time complexity
        # O(m*n * 4 * len(word))
        # cos for each word we will always check 4 direction, so we need factor this << recursion call into the time

        # space complexity
        # O(len(word))


    