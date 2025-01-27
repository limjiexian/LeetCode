# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # # preorder -> root/head of the tree or each
        # # inorder -> give us info about the number of nodes in each subtree

        # # base case
        # if not preorder or not inorder:
        #     return None
        
        # # when it comes to recursive we think of what we will do in the first iteration
        # # take root node
        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])

        # # preorder[0] our root node
        # # now we want construct our left subtree of our root node
        # # mid not only represent the position of root node val in inorder list, it also represent the number of nodes in left subtree
        # # inorder = [2,1,3,4], if mid = index 1 == [2,|1|,3,4] means left subtree will have node 2 aka 1 node in our subtree
        # # therefore we pass in preorder[1:mid+1]

        # # pass in inorder[:mid] instead of inorder[:mid+1] cos we dont want include mid as mid is the root node
        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # return root
    
        """ 27/1 """

        # preorder tells you the first node or the root node of each subtree
        
        # inorder tells information such as how many nodes are in left or right subtree
        #     - 2 1 3
        #     - so if u know the root node e.g. node 1 here, in order  will tell u left subtree of node 1 contains what nodes
        

        # base case is if preorder or in order is empty then it means no more nodes for us to create so we return
        if not preorder or not inorder:
            return
        
        # use preorder to get the root node
        root = TreeNode(preorder[0])

        # we find the index that our root node is located at in inorder list
        # everything on the left will be the left subtree for this root node
        # everything on the right will be the right subtree for this root node
        m = inorder.index(preorder[0]) 

        # recursively build our trees
        # go left and build our left subtree using to segement our arrays
        # m represent the number of nodes in our left subtree right so we will use this to slice our preorder array
        #   - we do m + 1 to account for the not inclusive for slicing
        # for inorder we dont do m+1 cos, m is the root node, and we alr created that so we dont need it
        root.left = self.buildTree(preorder[1:m+1], inorder[:m])
        # right is simply the remaining elements
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
    
        return root