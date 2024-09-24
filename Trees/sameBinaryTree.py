# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # given two roots of two binary trees p and q
        # check if these two trees are equivalent: aka exact nodes structure and same node value

        # just traverse through both tree at the same time recursively?
        # if they are the diff then just return false

        # base case
        if not p and not q:
            return True

        if not p or not q:
            return False

        
        if p.val != q.val:
            return False
        
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return (left and right)