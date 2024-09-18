# from typing import List

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # h > 0 > 1 > 2 > 3

#         # we want to turn 0 > 1 to 0 > none 
#         # aka none < 0

#         prev, curr = None, head

#         while curr:
#             # we need save the link to 1 first
#             temp = curr.next    # temp @ node 1

#             # now change node 0 to point to None aka prev
#             curr.next = prev

#             # now that we have 0 > None
#             # we need update prev and curr so that it can be ready for next iteration
#             # currently, curr = node 0, prev = None
            
#             prev = curr
#             curr = temp
#             # after update we have, prev @ node 0, curr @ node 1

#         return prev

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize prev to None (this will be the new tail of the reversed list)
        # and cur to head (the starting point of the list we need to reverse).
        prev, cur = None, head
        
        # Helper function for recursion that takes the current node (cur)
        # and the previous node (prev).
        def reverse(cur, prev):
            # Base case: when we reach the end of the list (cur is None),
            # return prev, which will be the new head of the reversed list.
            if cur is None:
                return prev
            else:
                # Store the next node in a temporary variable before breaking the link.
                temp = cur.next
                
                # Reverse the current node's link: point cur.next to the previous node.
                cur.next = prev
                
                # Recursively call reverse for the next node (temp) with the current node (cur)
                # as the new "prev".
                return reverse(temp, cur)

        # Start the recursion with the initial head of the list and prev as None (since there's no previous node yet).
        return reverse(head, None)