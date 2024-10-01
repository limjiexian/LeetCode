from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
MY SOLUTION USING BFS METHOD, NEETCODE USES DFS
"""
class Codec:
    # Encodes a tree to a single string.
    # basically convert tree structure into a sequence of bits -> so that we can send to another network and be reconstructed
    def serialize(self, root: Optional[TreeNode]) -> str:
        # bfs traversal
        # we will store our information in a level traversal format
        # e.g. root node, left child node, right child node, left child child node, right child child node

        if not root:
            return ""

        q = deque([root])
        res = []

        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        
        # above current code will end up with "1,2,3,null,null,4,5,null,null,null,null"
        # Remove trailing "null" values to avoid over-serialization
        while res and res[-1] == "null":
            res.pop()

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        if data == "":
            return None

        # result will become = [1,2,3,null,null,4,5,] 
        result = data.split(",")
        
        # convert the result to a mix of integers and None
        converted = []
        for i in result:
            if i != "null":
                converted.append(int(i))
            else:
                converted.append(None)

        # use deque to help track and create our binary tree
        q = deque()

        if not converted:
            return None
        
        # create root node
        rootNode = TreeNode(converted[0])
        q.append(rootNode)
        i = 1

        while q and i < len(converted):
            node = q.popleft()

            # process node de left child
            if i < len(converted) and converted[i] is not None:
                leftNode = TreeNode(converted[i])
                node.left = leftNode
                q.append(leftNode)
            
            i += 1

            # process node de right child
            if i < len(converted) and converted[i] is not None:
                rightNode = TreeNode(converted[i])
                node.right = rightNode
                q.append(rightNode)
            
            i += 1

        return rootNode

# time complexity: as we process each node, O(n)
# space complexity: the max number of nodes we will store in our deque will be O(n/2) approximate to O(n).

# Space complexity explanation:
# The queue (deque) stores nodes level by level during BFS.
# In a complete binary tree, the last level has up to n/2 nodes.
# Therefore, the maximum space used by the queue is O(n).
# Additionally, the result list also stores all n nodes, contributing to O(n) space.


            

"""
My attempt at using DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # dfs preorder
        # process first then go left and right
        res  = []

        def dfs(root):
            
            # base case
            if not root:
                res.append("N")
                return None
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        
        return ",".join(res)

        #[1, 2, N, N, 3, 4, N, N, 5, N, N]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        result = data.split(",")
        converted = []

        for i in result:
            if i != "N":
                converted.append(int(i))
            else:
                converted.append(i)
        
    
        def dfs():
            
            if converted[0] == "N":
                return None
            
            # construct
            root = TreeNode(converted[0])
            
            converted.pop(0) 
            root.left = dfs() # [2, N, N, 3, 4, N, N, 5, N, N]
            
            converted.pop(0)
            root.right = dfs()

            return root
        
        return dfs()
"""

"""
Neetcode Version
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
"""     
