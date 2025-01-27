# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        # last node that is being popped will be our visible node

        res = []

        if not root:
            return res

        q = deque()
        q.append(root)

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                
            res.append(node.val)
        
        return res



        