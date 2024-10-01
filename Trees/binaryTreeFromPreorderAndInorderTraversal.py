# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # preorder -> root/head of the tree or each
        # inorder -> give us info about the number of nodes in each subtree

        # base case
        if not preorder or not inorder:
            return None
        
        # when it comes to recursive we think of what we will do in the first iteration
        # take root node
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # preorder[0] our root node
        # now we want construct our left subtree of our root node
        # mid not only represent the position of root node val in inorder list, it also represent the number of nodes in left subtree
        # inorder = [2,1,3,4], if mid = index 1 == [2,|1|,3,4] means left subtree will have node 2 aka 1 node in our subtree
        # therefore we pass in preorder[1:mid+1]

        # pass in inorder[:mid] instead of inorder[:mid+1] cos we dont want include mid as mid is the root node
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root