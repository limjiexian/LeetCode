# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth(node, k):
            while node and k > 0:
                k-=1
                node = node.next
            
            return node

        dummy = ListNode(0, head)
        grp_prev = dummy

        while True:
            kth_node = get_kth(grp_prev, k)

            if not kth_node:
                break
            
            grp_next = kth_node.next

            prev, curr = kth_node.next, grp_prev.next

            while curr != grp_next:
                tmp = curr.next
                curr.next = prev

                prev = curr
                curr = tmp

            tmp = grp_prev.next     # node 1
            grp_prev.next = kth_node
            grp_prev = tmp

        return dummy.next
