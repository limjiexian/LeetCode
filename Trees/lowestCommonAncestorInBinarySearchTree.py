# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Given:
        # A BST with unique nodes value
        # 2 Nodes from tree p and q
        # Goal: 
        # Return lowest common ancestor (LCA) of the two nodes
        # LCA = lowest node in the tree such that both p and q are descendants
        # ancenstor is allowed tobe a descendant of itself
        # like LCA of p and q, there is a situation whereby p is the ancestor of q, so LCA will be = p

        # basically search for the parent node of p and q
        # edge case -> when p or q is the parent node

        # base case
        if (p.val >= root.val and q.val <= root.val) or (p.val <= root.val and q.val >= root.val):
            return root
        
        # if root node is bigger than both p and q, we will explore left subtree as left subtree contains node value smaller than the root node
        if root.val > p.val and root.val > q.val:
            lcaNode = self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            lcaNode = self.lowestCommonAncestor(root.right, p, q)

        return lcaNode