# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # return true if height is balanced
        # balanced height: left and right subtrees of every node differ in height by only 1

        # recursive go all the way down to bottom most node
        # if left and right subtree nth then return none
        # then check left return height with right return height, diff must not be more than 1
        self.unbalanced = False

        def dfs(curr: Optional[TreeNode]) -> int:
            # base case
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            if abs(left-right) > 1:
                self.unbalanced = True
            
            return max(left+1, right+1)

        dfs(root)

        # if self.unbalanced:
        #     return False
        # else:
        #     return True

        return not self.unbalanced



        