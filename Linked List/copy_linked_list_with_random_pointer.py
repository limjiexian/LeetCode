"""
# Definition for a Node.
"""
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # example 1: 
        # 3 -> 7 -> 4 -> 5 -> null

        """ Using Deque """
        # # NOTES: 
        # # YOU DONT NEED DEQUE COS, normally we use deque to ensure that our order is correct 
        # # but cos ll naturally its order is alr correct so we dont need it

        # if head == None:
        #     return None

        # old_two_new = {}
        # q = deque()
        # old_two_new[head] = Node(head.val)
        # q.append(head)

        # while q:
        #     curr = q.popleft()      # old 3
        #     curr_next = curr.next   # old 7

        #     if curr_next == None:   # e.g. old 5 next will be == None
        #         old_two_new[curr].next = None   # so we set new 5 next = None
        #         continue

        #     # if dont exist then we create a copy of it
        #     if curr_next not in old_two_new:                    # check if new copy of old 7 has been created
        #         old_two_new[curr_next] = Node(curr_next.val)    # if haven, then we create new copy of old 7
        #         q.append(curr_next)                             # append old 7 into queue

        #     old_two_new[curr].next = old_two_new[curr_next]     # set new copy of 3, its next, point to new copy of old 7


        # # End of while q loop means we every node has its own copy
        # # just that the .random haven set to point to the right nodes

        # curr = head     # old node 3

        # while curr:
        #     if curr.random == None:
        #         old_two_new[curr].random = None
        #     else:    
        #         old_two_new[curr].random = old_two_new[curr.random]

        #     curr = curr.next
        
        # return old_two_new[head]

        """ Two Pass using Normal Loop with if statement to check None """

        # curr = head
        # old_to_new = {}

        # while curr:
        #     new = Node(curr.val)
        #     old_to_new[curr] = new

        #     curr = curr.next
    
        # curr = head
        
        # while curr:
        #     # next pointer
        #     if curr.next == None:
        #         old_to_new[curr].next = None
        #     else: 
        #         old_to_new[curr].next = old_to_new[curr.next]

        #     # random pointer
        #     if curr.random == None:
        #         old_to_new[curr].random = None
        #     else:
        #         old_to_new[curr].random = old_to_new[curr.random]

        #     curr = curr.next

        # return old_to_new[head] if head != None else None


        """ Two Pass using Normal Loop using {none:none}"""
        old_to_new = {None : None}

        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            # next pointer
            old_to_new[curr].next = old_to_new[curr.next]

            # random pointer
            old_to_new[curr].random = old_to_new[curr.random]

            curr = curr.next

        return old_to_new[head] if head != None else None









