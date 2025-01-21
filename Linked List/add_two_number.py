# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        """ My Method """
        # # given 2 ll
        # # reverse both ll
        # # then for each ll combine their digits together
        # # and then sum them

        # def reverse(head):
        #     # None    1   2
        #     # prev    c   t

        #     prev, curr = None, head

        #     while curr:
        #         temp = curr.next
        #         curr.next = prev

        #         prev = curr
        #         curr = temp

        #     return prev
        
        # def get_num(head):
        #     total = 0
            
        #     curr = head

        #     while curr:
        #         num = curr.val
        #         total *= 10
        #         total += num

        #         curr = curr.next
            
        #     return total

        # l1 = reverse(l1)
        # l2 = reverse(l2)

        # num_one = get_num(l1)
        # num_two = get_num(l2)

        # two_sum = num_one + num_two

        # dummy = res = ListNode()

        # if two_sum == 0:
        #     return ListNode(0)

        # while two_sum:
        #     num = two_sum % 10

        #     res.next = ListNode(num)
        #     res = res.next

        #     two_sum //= 10

        # return dummy.next 

        """ Neetcode """

        dummy = curr = ListNode()

        carry = 0
        while l1 or l2 or carry:
            # get current val
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            
            # update pointer
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next 























