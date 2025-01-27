# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        left_limit = float("-inf")
        right_limit = float("inf")


        def dfs(node, left_limit, right_limit):
            if not node:
                return True
            
            if left_limit >= node.val or node.val >= right_limit:
                return False

            # go left
            # right_limit = min(node.val, right_limit)
            if not dfs(node.left, left_limit, min(node.val, right_limit)):
                return False

            # go right
            # left_limit = max(node.val, left_limit)
            if not dfs(node.right, max(node.val, left_limit), right_limit):
                return False
            
            return True
        
        return dfs(root, left_limit, right_limit)