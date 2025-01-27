# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(curr):
            if not curr:
                res.append("N")
                return
            
            res.append(str(curr.val))

            dfs(curr.left)
            dfs(curr.right)
        
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0
        vals = data.split(",")

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            root = TreeNode(int(vals[self.i]))
            self.i += 1

            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()







