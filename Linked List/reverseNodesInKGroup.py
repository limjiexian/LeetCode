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

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = curr = head
        first = 0
        listOfLL = []

        while start:
            count = 0

            # pass in curr = 1
            while count < k-1 and curr:
                curr = curr.next
                count += 1

            if curr is None:
                reversedHead, reversedTail = start, curr
                listOfLL.append((reversedHead, reversedTail))
                break

            temp = curr.next    # 4
            curr.next = None    # 3 > None
            reversedHead, reversedTail = self.reverse(start)    # pass in 1 > 2 > 3
            listOfLL.append((reversedHead, reversedTail))

            start = curr = temp
            count = 0

        # link all the ll together
        i = 0
        firstHead, firstTail = listOfLL[0]

        while i < len(listOfLL):
            rHead1, rTail1 = listOfLL[i]
            rHead2, rTail2 = listOfLL[i+1] if i+1 < len(listOfLL) else (None, None)

            if rTail1 is not None:
                rTail1.next = rHead2

            i += 1

        return firstHead
            

    def reverse(self, head) -> Optional[ListNode]:
        tail, curr = head, head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev, tail
