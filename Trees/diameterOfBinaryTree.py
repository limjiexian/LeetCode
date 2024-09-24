# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = length of the longest path between any two nodes within the tree
        self.maxDiameter = 0

        def dfs(curr) -> int:

            # base case
            if not curr:
                return 0 
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.maxDiameter = max(self.maxDiameter, left+right)

            return max(left+1, right+1)
        
        dfs(root)

        return self.maxDiameter