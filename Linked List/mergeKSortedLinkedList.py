from typing import Optional, List

# # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def merge(self, l1: ListNode, l2: ListNode) -> Optional[ListNode]:
        
#         # edge case
#         if l1 is None:
#             return l2
#         elif l2 is None:
#             return l1

#         temp = node = ListNode(0)

#         c1, c2 = l1, l2

#         while c1 and c2:
#             if c1.val <= c2.val:
#                 temp.next = c1
#                 c1 = c1.next
#             else:
#                 temp.next = c2
#                 c2 = c2.next

#             temp = temp.next

#         temp.next = c1 if c1 else c2

#         return node.next

#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         # given an array of k linked list
#         # so a list of linked list of size k
#         # each list is sorted in increasing order
#         # goal -> merge all the linked list into a mega linkedlist whereby it is sorted in increasing order for each node

#         # lets try merging 2 linkedlist together at a time
#         if not lists:
#             return None
            
#         size = len(lists) - 1

#         i = 1
#         newL = lists[0]

#         while i <= size:
#            # merge newL with l1
#             l1 = lists[i]
#             newL = self.merge(newL, l1)
#             i += 1

#         return newL.next

# # Helper function to convert Python list to linked list
# def convert_list_to_linked_list(arr):
#     if not arr:
#         return None
#     head = ListNode(arr[0])
#     current = head
#     for val in arr[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head            

# # Example usage
# sol = Solution()
# lists = [[-4, -2, 1, 3, 5], [-1, 24, 25], [7], [8], [7], [6], [-7], [-8], [-7], [-6]]

# # Convert each Python list to a linked list
# linked_lists = [convert_list_to_linked_list(l) for l in lists]

# output = sol.mergeKLists(linked_lists)


""" 
Above method time complexity is O(K*N) which is bad. 

We want to use merge sort algo to do this, which makes it log k cos k/2/2/2/2/2/2 keep divide by 2

"""

# O(log k solution)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        # basically do like merge sort
        while len(lists) != 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                
                merged = self.merge(l1, l2)
                mergedList.append(merged)

            lists = mergedList

        return lists[0]

    
    # merge 2 list together
    def merge(self, list1: ListNode, list2: ListNode) -> Optional[ListNode]:
        dummy = tail = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next