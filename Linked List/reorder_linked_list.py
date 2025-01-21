# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #                       f
        # [0, 1, 2, 3, 4, 5, 6]
        #           s
        #                 f
        # [0, 1, 2, 3, 4, 5 ]
        #        s

        # jsut need to split them into two half
        # then have l, r pointer and traverse both together
        
        # but qns is how do we know where is the middle point
        # another thing is how do i reach 6, and if i reach 6, i cant reverse back cos this is a singly linkedlist

        # what we need to do is to reverse the 2nd half linkedlist node
        # then we merge them together

        # we can use floyd tortoise and hare algo to find our mid point and then from there we do the reversal

        # find 1st half and 2nd half ll
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next      # slow represent the last node of 1st half ll

        slow.next = None    # break up the link between 1st and second half
    
        # reverse 2nd half set
        prev = None
        curr = l2

        while curr:
            temp = curr.next
            curr.next = prev
            
            prev = curr
            curr = temp
        
        l2 = prev

        # [0, 1, 2, 3]
        # [6, 5, 4]



        # [2, 4]
        # [8, 6]        

        """ My method """
        # start = res = ListNode()


        # while l1 and l2:
        #     # take one node from l1
        #     res.next = l1
        #     l1 = l1.next
            
        #     # update res
        #     res = res.next

        #     # take one node from l2
        #     res.next = l2
        #     l2 = l2.next

        #     res = res.next
        
        # if l1:
        #     res.next = l1

        # head = start.next

        # return None

        """ Neetcode """
        
        first = l1
        second = l2

        while second:
            f_next, s_next = first.next, second.next

            # combine to get first -> second -> original first.next
            first.next = second
            second.next = f_next

            # update first and second pointer
            first = f_next
            second = s_next

        
    
















