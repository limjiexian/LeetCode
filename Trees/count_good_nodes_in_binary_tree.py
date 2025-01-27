# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """ With Global Variable """
        # self.good_node = 0

        # if not root:
        #     return 0
    
        # def dfs(node, max_val):
        #     if not node:
        #         return 
            
        #     if max_val <= node.val:
        #         self.good_node += 1
            
        #     max_val = max(max_val, node.val)
        
        #     dfs(node.left, max_val)
        #     dfs(node.right, max_val)


        # dfs(root, -999)                        

        # return self.good_node


        """ Without Global Variable """
        
        if not root:
            return 0

        def dfs(node, max_val):
            if not node:
                return 0 
            
            count = 0

            if node.val >= max_val:
                count += 1
            
            max_val = max(max_val, node.val)
            
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)

            return count
        
        return dfs(root, -999)