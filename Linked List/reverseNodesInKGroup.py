from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# go through the entire LL
# after traversing K node, we send this K nodes into our reverse function and then append the reversed set into listOfLL
# once we processed all the set
# then we go through the list of LL to connect these sets together and return the head of the combined set

# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         start = curr = head
#         first = 0
#         listOfLL = []

#         while start:
#             count = 0

#             # pass in curr = 1
#             while count < k-1 and curr:
#                 curr = curr.next
#                 count += 1

#             if curr is None:
#                 reversedHead, reversedTail = start, curr
#                 listOfLL.append((reversedHead, reversedTail))
#                 break

#             temp = curr.next    # 4
#             curr.next = None    # 3 > None
#             reversedHead, reversedTail = self.reverse(start)    # pass in 1 > 2 > 3
#             listOfLL.append((reversedHead, reversedTail))

#             start = curr = temp
#             count = 0

#         # link all the ll together
#         i = 0
#         firstHead, firstTail = listOfLL[0]

#         while i < len(listOfLL):
#             rHead1, rTail1 = listOfLL[i]
#             rHead2, rTail2 = listOfLL[i+1] if i+1 < len(listOfLL) else (None, None)

#             if rTail1 is not None:
#                 rTail1.next = rHead2

#             i += 1

#         return firstHead
            

#     def reverse(self, head) -> Optional[ListNode]:
#         tail, curr = head, head
#         prev = None

#         while curr:
#             temp = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp

#         return prev, tail


"""
NEET CODE SOLUTION WITH EXPLANATION 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # instead of starting with prev = NONE, our first prev will always be pointing to kth.next
            # 1 > 2 > 3 > 4 > 5 > 6
            # After reverse we will always have 1 pointing to 4 = kth.next

            prev, curr = kth.next, groupPrev.next
            # reverse
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
        
            # link them after reversing
            # now curr will be at node = 3
            # 3 > 2 > 1        4 > 5
            # at first groupPrev will be = dummy
            # and that groupPrev.next is same as dummy.next which is node = 1
            # so we want dummy to point to 3
            temp = groupPrev.next # save temp = node = 1
            groupPrev.next = kth
            groupPrev = temp # move groupPrev to 1 node before kth which is node 1
        
        return dummy.next


    # receive dummy 1 > 2 > 3
    # thats why dont need k-1
    # cos we actually need run 3 iteration to get node 3 aka our kth node    
    def getKth(self, curr, k) -> Optional[ListNode]:
        count = 0
        
        while curr and count < k:
            curr = curr.next
            count += 1
        
        return curr 

    # def getKth(self, curr, k):
    #     while curr and k > 0:
    #         curr = curr.next
    #         k -= 1
    #     return curr