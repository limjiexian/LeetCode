from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # input range 1 to n
        # nums size == n + 1

        # cos max size is n+1
        # and we have max num be n
        # means means every number will point to a valid index

        # each num is unique BUT one num will be repeated 

        """ O(n) time and space """
        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num
            
        #     seen.add(num)


        """ O(n) time, O(1) space """

        # use floyd tortise and hare algo

        # treat nums = [1,2,3,2,2] as a linkedlist 

        # we start at index 0 and the element at each index we will be our next index destination, so if there exist a loop
        # it means this number is repeated
        
        # how do we detect this loop? -> floyd tortise and hare aglo -> slow and fast pointer


        slow, fast = 0, 0   

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow_two = 0

        while slow != slow_two:
            slow = nums[slow]
            slow_two = nums[slow_two]

        return slow
        









