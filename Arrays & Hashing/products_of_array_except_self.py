class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given
            - nums
        
        Task
            - output
                - output[i] == product of all the element of nums except nums[i]
            
        Follow up
            - do it in O(n) time without division operation
        
        """

        """ Prefix & Suffix """
        # output = [1] * len(nums)
        # prefix_product = [1] * len(nums)
        # suffix_product = [1] * len(nums)
        # i = 0
        # prefix_total = 1
        # suffix_total = 1

        # for a in range(len(nums)):
        #     prefix_total *= nums[a]
        #     prefix_product[i] = prefix_total

        #     suffix_total *= nums[len(nums)-1-a]
        #     suffix_product[len(nums)-1-i] = suffix_total

        #     i += 1
        
        # print("prefix_product = ", prefix_product)
        # print("suffix_product = ", suffix_product)
        
        # for i in range(len(output)):
        #     left = 1
        #     right = 1

        #     if i-1 >= 0:
        #         left = prefix_product[i-1]
            
        #     if i+1 < len(nums):
        #         right = suffix_product[i+1]

        #     output[i] = left * right

        # return output

# @ 1
# - 2 * 4 * 6 = 48

# @ 2
# - 1 * 4 * 6 = 24

# prefix_product
# 1, 2, 8, 48

# suffix_product
# 48, 48, 24, 6

# x, i, x, x

        """ Prefix & Suffix O(1) Space"""
        n = len(nums)
        res = [0] * n
        
        prefix = 1
        for i in range(n):
            # [1, 2, 3, 4]
            # [1, 1, ?] -> res
            res[i] = prefix
            prefix *= nums[i] # so when we go next iteration, res[i] will always store prefix not including itself
        
        postfix = 1

        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        

