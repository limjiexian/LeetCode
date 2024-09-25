# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Given root of a binary tree
        # Goal: return true if it is a valid binary serach tree
        # BST
        # -> left subtree nodes de keys must be less than root key
        # -> right subtree nodes de keys must be larger than root key
        # -> both left and right subtress themselves must also be binary search trees

        leftVal = float('-inf')
        rightVal = float('inf')


        def dfs(root, leftVal, rightVal) -> bool:
            # base case
            if not root:
                return True

            if (not leftVal < root.val < rightVal):
                return False
            
            # leftVal < root.val < rightVal

            left = dfs(root.left, leftVal, root.val)
            right = dfs(root.right, root.val, rightVal)

            return (left and right)
        

        return dfs(root, leftVal, rightVal)

        