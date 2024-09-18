from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = node = ListNode()  # Dummy node for the merged list

        # Traverse both linked lists
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        # Append any remaining elements
        temp.next = list1 if list1 else list2
        
        return node.next  # Return the head of the merged list


# Helper function to convert a list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for value in lst:
        current.next = ListNode(value)  # Create a new node for each list element
        current = current.next
    return dummy.next  # Return the head of the created linked list

# Helper function to convert a linked list to a Python list for easy output
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Input lists
x1 = [1, 2, 4]
x2 = [1, 3, 5]

# Convert lists to linked lists
list1 = list_to_linked_list(x1)
list2 = list_to_linked_list(x2)

# Merge the linked lists
sol = Solution()
merged_head = sol.mergeTwoLists(list1, list2)

# Convert merged linked list back to list to display the result
print(linked_list_to_list(merged_head))  # Output: [1, 1, 2, 3, 4, 5]
