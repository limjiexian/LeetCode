from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Given: root of a non empty binary tree
        # Goal: return the max path sum of any non-empty path
        # Path: a sequence of nodes whereby each pair of adjacent nodes has an edge connecting to them
        # Path sum: the sum of the node's values in the path

        # Requirement -> node cannot repeat in a path aka must make sure there is no cycle

        # what we might need
        # a way to track if a node is repeated or if we are in a cycle
        # get the max path that are reacheable for each node
        # maybe solve using recursive dfs?
        # they want us to get the cumulated max node value NOT the # of edges

        res = [root.val]

        def dfs(root):
            # base case
            if not root:
                return 0

            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # special case (if u dont do this u wont get the correct ans)
            # leftMax or rightMax contains pathvalue = negative.
            # so e.g. if leftMax = -10, we do not want to calculate the latest maxpath for this subtree to be leftmax+ rightmax + root node
            # because this will not yield the latest maxpath. if we got negative for leftmax we should only do rightmax+root node val
            # therefore we need do the following
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            mergedVal = leftMax + rightMax + root.val
            largerSubtreeVal = max(leftMax, rightMax)

            # res will always contain the current maxPathValue that we found so far
            # therefore we need to check and update it after we process each set subtree
            res[0] = max(res[0], mergedVal)
        
            # we will return the path with the subtree that has the larger max path value
            return root.val + largerSubtreeVal

            # decide whether merging leftH and rightH path will yield a longer path or continue pass up the longer subtree path

        dfs(root)

        return res[0]