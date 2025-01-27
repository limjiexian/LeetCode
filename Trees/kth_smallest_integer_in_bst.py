# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """ Recursive DFS """
        # size = k
        # self.res = 0

        # def dfs(node, size):
        #     if not node:
        #         return size
            
        #     size = dfs(node.left, size)
        #     print("size = ", size)
        #     size -= 1
            
        #     if size == 0:
        #         self.res = node.val

        #     size = dfs(node.right, size)

        #     return size
        
        # dfs(root, k)

        # return self.res

        """ Iterative """
        stack = []
        curr = root
        size = k

        while curr or stack:
            
            # keep traverse left
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            size -= 1
            
            if size == 0:
                return curr.val
            
            curr = curr.right
