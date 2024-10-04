class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
    
        def dfs(i):

            # base case
            if i > len(nums) - 1:

                # in python
                # list1 = []
                # list2 = [1, 2]
                # list1.append(list2)
                # list1 will hold a reference to list2, not a copy of it.
                # so if u modify list2, the changes will be reflected in list1

                # When you want to add the current state of subset to the res list, 
                # you want to capture a snapshot of the current state of subset at that specific point in the recursion. 
                # If you were to append the subset directly without making a copy, 
                # further modifications to subset (such as pop()) would affect all previously stored versions of subset in res.
                res.append(subset.copy())
                return 
            
            # pick nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # dont pick nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)

        return res

# time complexity:
# we will call the recursion 2^n times because we have 2^n subset
# subset.copy() is called once for each of the subset generated. .copy() takes O(n) time to copy
# therefore total time complexity = O(n * 2^n)


# space complexity:
# space used for our recursion stack == depth of our recursion == n
# - The depth of the recursion is n because each level of the recursion corresponds to deciding whether to include 
# - or exclude the current element in the subset, and there are n elements in the nums list.

# space used for our res storage is 2^n, as we have 2^n subset
# so total space complexity is O(n + 2^n)