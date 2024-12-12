from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)

        i = 0 
        total = 0
        min_prefix = float('-inf')

        for num in nums:
            total += num
            prefix_sum[i] = total
            i += 1
        
        min_prefix = min(prefix_sum)
        offset = 1 - min_prefix
        
        return 1 if min_prefix > 0 else offset
