# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # h > 0 > 1 > 2 > 3

        # we want to turn 0 > 1 to 0 > none 
        # aka none < 0

        prev, curr = None, head

        while curr:
            # we need save the link to 1 first
            temp = curr.next    # temp @ node 1

            # now change node 0 to point to None aka prev
            curr.next = prev

            # now that we have 0 > None
            # we need update prev and curr so that it can be ready for next iteration
            # currently, curr = node 0, prev = None
            
            prev = curr
            curr = temp
            # after update we have, prev @ node 0, curr @ node 1

        return prev
