# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Node is good only if: path from root to node contains no node with a value greater than the node value itself
        # Goal: to return number of good nodes within the tree

        # Dont think BFS is the play
        # Think will need to use recursive dfs or something

        maxVal = -999
        self.count = 0
        def dfs(root, maxVal) -> int:
            
            # base case
            if not root:
                return 0

            if root.val >= maxVal:
                # good node
                self.count += 1

            # update maxVal
            maxVal = max(maxVal, root.val)

            # continue traverse down
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, maxVal)

        return self.count


"""
NEETCODE SOLUTION

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
    
        def dfs(root, maxVal) -> int:
            
            # base case
            if not root:
                return 0
            
            # preorder
            res = 1 if root.val >= maxVal else 0
            maxVal = max(maxVal, root.val)
            res += dfs(root.left, maxVal)
            res += dfs(root.right, maxVal)

            return res
    
        return dfs(root, root.val)

"""