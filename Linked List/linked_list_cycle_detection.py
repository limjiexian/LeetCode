# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        """ O(n) space using set() """
        # # if one node is visited twice == cycle
        # # index == start of the cycle
        # # index -1 == no cycle

        # # we traverse down the linkedlist then at any point of if we revisited a node == return True aka cycle
        # # set() to keep track of the node that we visited

        # visited = set()

        # curr = head

        # while curr:
        #     if curr in visited:
        #         return True

        #     visited.add(curr)

        #     curr = curr.next
        
        # return False

        """ O(1) space using floyd tortoise and hare algo """

        if head == None:
            return False
        
        curr = head

        slow, fast = curr, curr.next

        # need check both fast and fast.next
        # cos if we dont do that and only check for fast 
        # if we odnt check fast.next
        # and if we do fast.next.next
        # essentially we are doing None.next which is invalid

        while fast and fast.next:
            if slow == fast:
                return True

            slow, fast = slow.next, fast.next.next

        return False
