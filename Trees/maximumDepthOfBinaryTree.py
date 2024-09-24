# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth = # of nodes along the longest path from root node down to the farthest leaf node
        # goal is to return the depth of a binary tree

        if not root:
            return 0
        
        depthL = 1 + self.maxDepth(root.left)
        depthR = 1 + self.maxDepth(root.right)


        return max(depthL, depthR)