from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # given m x n 2d int array
        # a target integer
        # each row of the matrix is sorted in increasing order
        # first int of each row is greater than the last int of previous row
        # return true if target exists within the matrix, false if otherwise
        # sol must be in O(log(m*n))

        # using binary search on each row by only looking at their initial integer
        top, bot = 0, len(matrix) - 1
        
        while top <= bot:
            mid = (top + bot) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid + 1

        # After the loop, bot will be the row where the target could be located
        # Ensure bot is within bounds and the target could be in the matrix[bot] row
        if bot < 0 or bot >= len(matrix):
            return False
        
        # Second binary search to find the target within the row `bot`
        l, r = 0, len(matrix[bot]) - 1

        # so like even tho top and bot converge on a single row, we cant just return that single row, we need check inside the single row. to do that we make sure that the while loop dont terminate when we reach top <bot
        # but for search for min value, when l and r converge, that one is confirmed the min value so dont need check again
        while l <= r:
            mid = (l+r) // 2

            if matrix[bot][mid] == target:
                return True
            elif matrix[bot][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False


sol = Solution()
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3
output = sol.searchMatrix(matrix, target)