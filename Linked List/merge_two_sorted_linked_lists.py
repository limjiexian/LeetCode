# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        """ Using a new linkedlist """
# #              c
# #    N -> 1    2 -> 4
# #         1 -> 3 -> 5
# #         c
#         start = new_list = ListNode()

#         prev_one = None
#         prev_two = None

#         curr_one = list1
#         curr_two = list2


#         while curr_one and curr_two:

#             if curr_one.val <= curr_two.val:
#                 temp = curr_one.next
#                 curr_one.next = None
#                 new_list.next = curr_one
                
#                 curr_one = temp
#             else:
#                 temp = curr_two.next
#                 curr_two.next = None
#                 new_list.next = curr_two

#                 curr_two = temp
            
#             new_list = new_list.next
            

#         if curr_one:
#             new_list.next = curr_one
#         elif curr_two:
#             new_list.next = curr_two
#         else:
#             return start.next
        
#         return start.next

        """ Optimal new linkedlist """
        
        start = temp = ListNode()

        c1, c2 = list1, list2

        while c1 and c2:
            if c1.val <= c2.val:
                temp.next = c1
                c1 = c1.next
            else:
                temp.next = c2
                c2 = c2.next
            
            temp = temp.next
        
        temp.next = c1 if c1 else c2

        return start.next
    
    







        



