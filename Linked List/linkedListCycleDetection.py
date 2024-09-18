from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # given head, return true if cycle exist in the linked list
        # cycle: if at least one node can be visted again by following the next pointer

        # traverse through the list and then if any of the node got visted twice we return true

        curr = head
        visited = {}

        while curr:

            if visited.get(curr, 0):
                return True
        
            visited[curr] = visited.get(curr, 0) + 1
            curr = curr.next
        
        return False

