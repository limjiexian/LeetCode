# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res = float("-inf")
        self.res = float("-inf")

        def dfs(root):
            # nonlocal res

            if not root:
                return 0

            left_count = dfs(root.left)
            right_count = dfs(root.right)

            # Calculate the "horizontal" diameter through the current node
            horizontal = left_count + right_count

            # Update the maximum diameter
            self.res = max(horizontal, self.res)

            # Return the height of the subtree rooted at the current node
            return max(left_count, right_count) + 1

        dfs(root)  # Trigger the DFS traversal
        return self.res  # Return the maximum diameter
    

""" Without using any global variable """
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

#         def dfs(root, diameter):
#             if not root:
#                 return 0, 0

            
#             left_height, left_diameter = dfs(root.left, diameter)
#             right_height, right_diameter = dfs(root.right, diameter)

#             curr_diameter = left_height + right_height
            
#             diameter = max(curr_diameter, left_diameter, right_diameter)
#             height = max(left_height, right_height) + 1

#             return height, diameter
        
#         h, d = dfs(root, 0)

#         return d
        