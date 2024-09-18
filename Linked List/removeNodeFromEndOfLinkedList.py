from typing import Optional

Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node that points to head to handle edge cases (like removing the first node)
        dummy = ListNode(0)
        dummy.next = head
        curr = target = head
        prev = dummy
        
        count = 0
        while curr and curr.next:
            # Move our target pointer after we reach n-1 steps from curr
            if count >= n - 1:
                prev = target
                target = target.next

            curr = curr.next
            count += 1
        
        # prev is now pointing to the node before the one we want to remove
        prev.next = prev.next.next
        
        # Return the modified list, skipping the dummy node
        return dummy.next