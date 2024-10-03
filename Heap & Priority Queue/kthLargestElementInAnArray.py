import heapq
from typing import List


""" Heap method """
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # Given an unsorted array of integers nums and integer k
#         # return K largest element in the array
#         newNums = []
#         for num in nums:
#             newNums.append(-1 * num)

#         heapq.heapify(newNums)

#         for i in range(k):
#             target = heapq.heappop(newNums)
        
#         return -1 * target


""" Neetcode Quickselect method"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # why we take size - k?
        # because e.g. size is 6
        # and they want k=2 aka 2nd largest, this means it will be at index 4
        k = len(nums) - k

        # p will be our swap pointer
        # l will be our traverse pointer
        def quickSelect(l, r):
            p, pivot = l, nums[r]

            # not inclusive of r cos r is our pivot de index
            for i in range(l, r):
                # basically the array will be in increasing order
                # if less than means we put nums[i] to nums[p]
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
               
            # last step, swap nums[p] with nums[r]
            nums[p], nums[r] = nums[r], nums[p]

            # p > k we go left, cos left parition array will contain our target 
            if p > k:
                return quickSelect(l, p-1)
            elif p < k:
                return quickSelect(p+1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums)-1)
        
# avg time complexity for quick select is O(n) because u recursively call and traverse with size -> n + n/2 + n/4 + ... = ~ O(n)
# worst case time complexity for quick select is O(n^2) because if each partition u only managed to partition into, left side is 1, right size is n-1, and that u keep have to go
# into right side. so u have to traverse thru size of n-1 + n-2 + n-3 ... for each recursion function 
                
