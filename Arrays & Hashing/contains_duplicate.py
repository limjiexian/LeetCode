from typing import List

""" BRUTE FORCE METHOD -> O(n^2), some test case will get time out"""
# class Solution:
#     def containsDuplicate (self, nums: List[int]) -> bool:
#     # integer array nums
#     # return T if any value repeated twice in the array
#     # return F if every element is distinct

#         # Bruteforce method
#         # for each element at index i, compare it with i+1~end
#         # if same return false, else continue until i=end
#         size = len(nums)
#         for i in range(size):
#             for j in range(i+1, size):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
    
# nums = [1,2,3,1]
# sol = Solution()

# results = sol.containsDuplicate(nums)
# print(results) 

""" Hashing method """
class Solution:
    def containsDuplicate (self, nums: List[int]) -> bool:
    # integer array nums
    # return T if any value repeated twice in the array
    # return F if every element is distinct

        distinct = set()
        size = len(nums)
        for i in range(size):
            if nums[i] not in distinct:
                distinct.add(nums[i])
            else: return True
        return False 
    
nums = [1,2,3,1]
sol = Solution()

results = sol.containsDuplicate(nums)
print(results)  