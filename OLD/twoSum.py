from typing import List

# First Attempt
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         size = len(nums)

#         for i in range(size):
#             if i == len(nums)-1:
#                 break
#             first = nums[i]

#             for j in range(size):
#                 if i+j+1 > size-1:
#                     break
#                 second = nums[i+j+1]
#                 if first + second == target:
#                     return [i, i+j+1]

# Cleaner Code
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         size = len(nums)
#         for i in range(size):
#             num1 = nums[i]
#             for j in range(i+1, size):
#                 num2 = nums[j]
#                 if num1 + num2 == target:
#                     return [i, j]

# Hash Approach
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         memo = {}
#         for i, j in enumerate(nums):
#             second = target - j
#             if second in memo:
#                 return [i, memo[second]]
#             else:
#                 memo[j] = i

# Hash Approach if they want you to return in ascending order
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        for i, j in enumerate(nums):
            second = target - j
            if second in memo:
                return [i, memo[second]] if i < memo[second] else [memo[second], i]
            else:
                memo[j] = i

            
nums = [2,7,11,15] 

# i=0, j=2
# i=1, j=7
# i=3, j=11
# i=4, j=15

target = 9

# nums = [3,3]
# target = 6

sol = Solution()

results = sol.twoSum(nums, target)
print(results)