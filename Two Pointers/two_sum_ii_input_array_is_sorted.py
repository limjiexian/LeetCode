from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """ Brute Force """
        # for i in range(len(numbers)):
        #     for j in range(i, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i+1, j+1]


        """ Two Pointer """
        l, r = 0, len(numbers)-1

        while l < r:
            two_sum = numbers[l] + numbers[r]
        
            if two_sum == target:
                return [l+1, r+1]

            if two_sum > target:
                r -= 1
            else:
                l += 1
            
