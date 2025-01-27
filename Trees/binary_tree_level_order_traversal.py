# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        res = []

        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            sol = []
            for i in range(len(q)):
                node = q.popleft()
                sol.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            res.append(sol)
        
        return res
