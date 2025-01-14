from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        """ Binary Search 2D ver """
        l, r = 0, len(matrix)-1

        while l <= r:
            m = (l+r) // 2

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break

        target_arr = matrix[m]
        l, r = 0, len(target_arr)-1

        while l <= r:
            m = (l+r) // 2

            if target < target_arr[m]:
                r = m - 1
            elif target > target_arr[m]:
                l = m + 1
            else:
                return True
        
        return False
