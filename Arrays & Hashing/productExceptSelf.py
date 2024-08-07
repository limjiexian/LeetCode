from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # integer array nums, return answer such that
        # answer = product of all elements of nums except nums[i]
        # must be in o(n) time without division operation

        size = len(nums)

        prefix = [0] * size
        postfix = [0] * size
        output = [0] * size

        prefix_sum = 1
        postfix_sum = 1

        for i in range(size):
            j = -i - 1

            prefix[i] = prefix_sum
            postfix[j] = postfix_sum

            prefix_sum *= nums[i]
            postfix_sum *= nums[j]

        # longer ver
        # i=0
        # for l, r in zip(prefix, postfix): 
        #     output[i] = l*r
        #     i+=1
        #     if i == size:
        #         break

        # shorter ver
        # the reason why we need use zip is cos if we dont use it, they will just iterate over prefix and postfix INDEPENDENTLY rather than pairing the elements
        # Python, when you write for a, b in some_iterable, the iterable some_iterable should yield pairs of elements (like tuples), which isn't directly the case for two separate lists.
        output = [l*r for l,r in zip(prefix, postfix)]

        return output


sol = Solution()
# input = [-1,1,0,-3,3]
input = [1,2,3,4]

output = sol.productExceptSelf(input)

print(output)