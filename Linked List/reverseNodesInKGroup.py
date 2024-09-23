from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # given head of a singly linked list
        # and a positive integer k
        # u must reverse first k nodes in the linkedlist
        # and then reverse the next k nodes
        # if k = 3
        # 1 > 2 > 3 > 4 > 5 > 6
        # 3 > 2 > 1 > 6 > 5 > 4

        # if fewer than k nodes then dont reverse
        # return the modified list after reversing

        curr = head

        while curr:
            
            # come in
            # 1 > 2 > [3]
            # temp = [3].next aka = 4
            # [3].next = None
            # pass in [1]
            # get back
            # 3 > 2 > 1
            # [1].next set to [4]

            # repeat above process until we reach the end
            # special case if count < k we simply dont touch

            # check if count < k
            count = 0
            start = curr

            while start:
                count += 1
                start = start.next

            if count < k:
                return head
            else:
                s, t = self.reverse(curr)
                t.next = start
                curr = start
                count = 0

            

    def reverse(self, list1: ListNode) -> (Optional[ListNode], Optional[ListNode]):

        prev, curr = None, list1
        tail = list1

        while curr:        
            temp = curr.next    
            curr.next = prev
            prev = curr
            curr = temp
        
        head = prev

        return head, prev   # node 3 and node 1


    





            