# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# recursive dfs in order 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Given root of a BST, integer k
        # Goal: return the kth smallest value (1-indexed) in the tree
        # 1-indexed means it count from 1 instead of 0
        self.k = k 
        self.count = 0
        self.target = 0

        def dfs(root):

            if not root:
                return
            
            dfs(root.left)
            
            self.count += 1
            if self.count == self.k:
                self.target = root.val
                return

            dfs(root.right)

        dfs(root)
        return self.target
            
            