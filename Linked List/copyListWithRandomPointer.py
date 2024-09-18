from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # given head of a linked list
        # each node contains additional pointer called random -> may point to any node in the list or NULL
        # task - create a deep copy of the list
        # deep copy: consist of exactly n new nodes
        # - None of the pointers in the new list should point to nodes in the original list.
        # - basically copy and create a new set with the same attributes

        curr = head
        newHead = Node(0)
        newCurr = newHead

        o2newMap = {} # old node pointer: new node pointer

        # first pass
        while curr: 
            # create our new node
            new = Node(curr.val)
            
            # update hash map for our newly created node
            o2newMap[curr] = new

            # update
            newCurr.next = new
            newCurr = newCurr.next

            curr = curr.next
        
        # second pass
        curr = head
        newCurr = newHead.next
        while curr:
            if curr.random is not None:
                getPointer = o2newMap[curr.random]
                newCurr.random = getPointer
            else:
                newCurr.random = None

            curr = curr.next
            newCurr = newCurr.next
            
        return newHead.next

            




