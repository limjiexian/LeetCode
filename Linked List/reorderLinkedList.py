# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # Given a linked list 
        # reorder the list into this format : 0, n-1, 1, n-2, 2, n-3, ...]  # n is length of the linked list

        # Attempt 
        # Split the original linked list into
        # front and back
        # front is just ur, 0, 1, 2, ... 
        # back is the n thingy: n-1, n-2, ... 
        # then combine front and back together alternating them starting with front

        # neetcode guy to identify the mid point by using slow, fast method
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow.next will be the first node of our back linkedlist that we want to reverse 

        second = slow.next
        slow.next = None

        prev = slow.next

        while second:
            temp = second.next  # 5
            second.next = prev
            prev = second
            second = temp
        
        # prev point to n node
        first, second = head, prev

        # 0 > 1 > 2 > 3 > 4 > 5 > 6

        # first : 0 > 1 > 2 > 3
        # second : 6 > 5 > 4 > None

        while second:
            tempFirst, tempSecond = first.next, second.next # node 1, node 5
            
            first.next = second     # 0 > 6 > 5 > 4
            second.next = tempFirst # 0 > 6 > 1 > 2 > 3

            # update our first and second for next iteration
            first = tempFirst   # 1 > 2 > 3
            second = tempSecond # 5 > 4


                        

            

