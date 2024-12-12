class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Given
            - nums -> int array

        Task
            - find a subarray that has the largest product within the array
        
        """

        """ for loop Brute force """

        # max_total = float('-inf')

        # for i in range(len(nums)):
        #     total = 1

        #     for j in range(i, len(nums)):
        #         total *= nums[j]
        #         max_total = max(max_total, total)   
        
        # return max_total

        """ 
        Prefix Suffix method
        4 observations
        1. all positive number -> result in +ve ans
        2. even # of negative numbers -> result in +ve ans
        3. odd # of negative numbers -> result in -ve ans
        4. any 0 -> result in 0
          - so we only want to count the subarray sequence that dont have 0

        Idea is that:
        if we got odd negative, we simply just ignore 1 of the negative
          - e.g. [1,-2, 3, -5, 6, 7, -3]
          - we try all 3 combi, that is ignore -2 first, see whats the max
          - then ignore -5 and so on. 
          - so how do we "ignore", by just calculating the prefix and suffix of that negative value

        """

        max_prefix = float("-inf")
        max_suffix = float("-inf")

        prefix = 1
        suffix = 1

        n = len(nums)

        for i in range(n):
            if prefix == 0:
                prefix = 1

            prefix *= nums[i]
            max_prefix = max(max_prefix, prefix)
        
        for i in range(n-1, -1, -1):
            if suffix == 0:
                suffix = 1

            suffix *= nums[i]
            max_suffix = max(max_suffix, suffix)


        return max(max_prefix, max_suffix)







