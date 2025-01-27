# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True

        if root.val == subRoot.val and self.check_subtree(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return (left or right)
        

    def check_subtree(self, p, q) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        left = self.check_subtree(p.left, q.left)
        right = self.check_subtree(p.right, q.right)

        return (left and right)
        
