# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        def dfs(root):
            if not root:
                return 0

            left_h = dfs(root.left)
            right_h = dfs(root.right)

            diff = abs(left_h-right_h)

            if diff > 1:
                self.res = False

            return max(left_h, right_h) + 1
        
        dfs(root)

        return self.res