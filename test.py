from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Given: 
        # - an integer array nums
        
        # Goal:
        # - return the length of the longest strictly increasing subsequence
        

        """ Brute Force """
    
        # # check if valid
        # def check_valid(array):
        #     i = 0
        #     while i+1 < len(array):
        #         if array[i] >= array[i+1]:
        #             return False

        #         i += 1

        #     return True

        # max_length = float('-inf')
        # sol = []

        # def dfs(i, max_length):
        #     # nonlocal max_length 

        #     if i == len(nums):
        #         if check_valid(sol):
        #             max_length = max(max_length, len(sol))
        #         return max_length
            
        #     # include
        #     sol.append(nums[i])
        #     l1 = dfs(i+1, max_length)
        #     sol.pop()

        #     # exclude
        #     return max(l1, dfs(i+1, max_length))

        # return dfs(0, max_length)

        # # return max_length


        """ With Cache """

        memo = {}
        max_num = float("-inf")

        def dfs(i, length, max_num):
            print()
            print(f"dfs({i})")

            if i == len(nums):
                return length

            if i in memo:
                return memo[i]

            # include
            include_len = length
            if max_num < nums[i]:
                print("include -> nums[i] = ", nums[i])
                print("include -> max_num = ", max(max_num, nums[i]))
                include_len = dfs(i+1, length+1, max(max_num, nums[i]))
                print()
                print(f"back to dfs({i})")

            # exclude
            print("exclude -> nums[i] = ", nums[i])
            print("exclude -> max_num = ", max_num)
            exclude_len = dfs(i+1, length, max_num)
            print()
            print(f"back to dfs({i})")
            

            memo[i] = max(include_len, exclude_len)

            return memo[i]
            
        dfs(0, 0, max_num)

        return memo[0]


# dfs(0)
# 1, 2

# 9
# dfs exclude 9
#     - dfs include 1
#         - 


s = Solution()
nums=[0,1,0,3,2,3]

s.lengthOfLIS(nums)

