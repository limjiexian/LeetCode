from typing import List

# # O(n) space
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # given an array of integers nums containing n + 1 integers
#         # each integer in nums is in the range of [1, n] inclusive
#         # each integer is unique EXCEPT for 1 integer which can appear two or more times
#         # task - return the integer that appears more than once

#         hashSet = {}
#         target = float('inf')

#         for num in nums:
#             if hashSet.get(num, 0) >= 1:
#                 target = num
            
#             hashSet[num] = hashSet.get(num, 0) + 1

#         return target


# O(1) space :

# idea is after u find the first interception of slow == fast
# the distance from slow2=0 to the beginning of the cycle is the same as the distance from slow to the beginning of the cycle
# so u just need increment both of them by 1 step, the moment they intercept that will be the number that is repeated
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        
        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow
