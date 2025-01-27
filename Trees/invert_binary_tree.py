# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

""" my ver but dont really need the storing of the node, can just swap them LOl """
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

#         def dfs(curr):
#             if curr == None:
#                 return None
            
#             left_node = dfs(curr.left)
#             right_node = dfs(curr.right)

#             curr.left = right_node
#             curr.right = left_node
            
#             return curr

#         return dfs(root)

""" Neetcode """
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # invert binary tree and return its root
        # lets try recursive

        # base case
        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root
