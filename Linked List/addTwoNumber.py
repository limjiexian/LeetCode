from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         # given 2 non empty linked list l1, l2 // they represent a non negative integer but this value is stored in reverse order
#         # e.g. 123 will be  3 > 2 > 1
        
#         num1 = []
#         num2 = []

#         curr1 = l1
#         curr2 = l2

#         while curr1:
#             num1.append(curr1.val)      # 1, 2, 3 will be stored as 3, 2, 1
#                                         # so we will have [3, 2, 1]
#             curr1 = curr1.next

#         while curr2:
#             num2.append(curr2.val)
#             curr2 = curr2.next
        
#         sum1 = 0
#         while num1:
#             zero = len(num1) - 1
#             last = num1.pop(-1)

#             sum1 += last * (10 ** zero)

#         sum2 = 0
#         while num2:
#             zero = len(num2) - 1
#             last = num2.pop(-1)

#             sum2 += last * (10 ** zero)

#         finalTotal = sum1 + sum2 # e.g. 975

#         if finalTotal == 0:
#             return ListNode(0)

#         newHead = ListNode()
#         curr = newHead

#         while finalTotal:
#             val = finalTotal % 10
#             node = ListNode(val)
#             curr.next = node
#             curr = curr.next

#             finalTotal = finalTotal // 10

#         return newHead.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
 
'''
Sum and Calculate Carry:

val = v1 + v2 + carry: We sum the values from l1, l2, and the carry.
carry = val // 10: If the sum is 10 or greater, this divides the sum by 10 to get the carry value (either 1 or 0).
val = val % 10: We use the remainder when dividing by 10 to get the current digit that will go in the new node.

 '''