# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        """ Two Pass"""
        # # given ll
        # # traverse to the nth node counting from the end of the list
        # # return ll head

        # # can just traverse to find out the total number of nodes
        # # total - n = X
        # # X.next is the nth node

        # # a   p   c
        
        # # 1   2   3   4
        
        # curr = head
        # total = 0

        # # get total no. of nodes
        # while curr:
        #     total += 1
        #     curr = curr.next

        # steps = total - n
        
        # # edge case
        # # if they only want us to remove the first node aka total == n
        # if total == n:
        #     return head.next

        # curr, prev = head, None

        # while curr:
        #     if steps == 0:
        #         break
            
        #     steps -= 1
        #     prev = curr
        #     curr = curr.next
        

        # prev.next = curr.next

        # return head


        """ Single Pass -> Two Pointer """

        dummy = ListNode(0, head)
        l, r = dummy, head
        count = 0 

        # move r to n steps away from l
        for i in range(n):
            r = r.next
        

        while r:
            r = r.next
            l = l.next
            count += 1

        # if n = 2, head = [1,2,3,4]
            # l           r
        # 1   2   3   4

        # if n =1, head = [5]
        # l       r
        # d   5

        l.next = l.next.next

        return dummy.next


