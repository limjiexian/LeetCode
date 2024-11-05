from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Given nums, find a subarray that has the largest product within the array and return it
        # subarray requirement:
        # - a non empty sequence of elements within an array


        # prefix suffix method
        # 4 observations
        # 1. all positive number -> result in +ve ans
        # 2. even # of negative numbers -> result in +ve ans
        # 3. odd # of negative numbers -> result in -ve ans
        # 4. any 0 -> result in 0
        #   - so we only want to count the subarray sequence that dont have 0

        # idea is that
        # if we got odd negative, we simply just ignore 1 of the negative
        #   - e.g. [1,-2, 3, -5, 6, 7, -3]
        #   - we try all 3 combi, that is ignore -2 first, see whats the max
        #   - then ignore -5 and so on. 
        #   - so how do we "ignore", by just calculating the prefix and suffix of that negative value

        prefix = float("-inf")
        res = 1
        for num in nums:
            if res == 0:
                res = 1
            
            res *= num
            prefix = max(prefix, res)

        suffix = float("-inf")
        res = 1
        for i in range(len(nums)-1, -1, -1):
            if res == 0:
                res = 1
            
            res *= nums[i]
            suffix = max(suffix, res)

        return max(prefix, suffix)




