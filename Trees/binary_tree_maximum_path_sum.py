# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the global maximum path sum
        self.res = float("-inf")

        def dfs(node):
            if not node:
                # Base case: no contribution from a null node
                return 0
            
            # Recursively find the max path sum of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Calculate the path sum through the current node (peak path)
            d = left + right + node.val

            # Update the global maximum path sum
            self.res = max(self.res, d)

            # Contribution to the parent: max of one side (left or right) + current node
            # Include max(0, ...) to ignore negative path sums
            return max(0, max(left, right) + node.val)
        
        # Perform DFS starting from the root
        dfs(root)

        # Return the global maximum path sum
        return self.res
