# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # [[1,2,4],[1,3,5],[3,6]]

        """  1st Approach: Iteratively Merge with a Single Result List """
        # def merge_ll(l1, l2):
        #     dummy = curr = ListNode()

        #     while l1 and l2:
        #         # if l1 smaller we take 1 node from l1 and link to curr
        #         if l1.val <= l2.val:
        #             curr.next = l1
        #             l1 = l1.next
        #         else:
        #             curr.next = l2
        #             l2 = l2.next
                
        #         curr = curr.next

        #     if l1:
        #         curr.next = l1
        #     elif l2:
        #         curr.next = l2
            
        #     return dummy.next
        
        # if len(lists) == 0:
        #     return None

        # res = lists[0]

        # for i in range(1, len(lists)):
        #     # print("res = ", res)
        #     # print("list[i] = ", list[i])
        #     # print()
        #     res = merge_ll(res, lists[i])

        # return res    

        """ 2nd Approach: Iteratively Merge Pairs of Lists"""
        def merge_ll(l1, l2):
            dummy = curr = ListNode()

            while l1 and l2:
                # if l1 smaller we take 1 node from l1 and link to curr
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                
                curr = curr.next

            if l1:
                curr.next = l1
            elif l2:
                curr.next = l2
            
            return dummy.next
        
        if len(lists) == 0:
            return None

        
        while len(lists) > 1:
            l1 = lists.pop(0)
            l2 = lists.pop(0)

            lists.append(merge_ll(l1, l2))

        return lists[0]




