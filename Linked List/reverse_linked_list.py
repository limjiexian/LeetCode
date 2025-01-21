# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
               
        # 0 -> 1 -> 2 -> 3
     
        # 3 -> 2 -> 1 -> 0


        # traverse the linkedlist
        # reverse connection for prev and curr 

        prev, curr = None, head

        while curr:

            temp = curr.next    # store curr.next node, so that we dont lose the connection
            curr.next = prev    # reverse the link from [prev -> curr] to [prev <- curr]

            prev = curr         # update curr and prev to prepare for next iteration
            curr = temp

        return prev







