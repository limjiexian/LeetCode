# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # given roots of two binary trees root and subRoot
        # return true if root have a subtree in it that is equivalent as the subRoot

        # traverse through Root until we find a node with the same value as subRoot node value
        # then do we do the comparison 

        valid = False
        q = deque()

        if root:
            q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.val == subRoot.val:
                    valid = self.checkTree(node, subRoot)
                    if valid:
                        return True
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

        return valid

    def checkTree(self, q: Optional[TreeNode], p: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        
        if not q or not p or (q.val != p.val):
            return False
        
        left = self.checkTree(q.left, p.left)
        right = self.checkTree(q.right, p.right)

        return (left and right)



