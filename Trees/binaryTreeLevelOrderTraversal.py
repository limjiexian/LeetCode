# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Given:
        # a binary tree root
        # Goal:
        # return the level order traversal of it as a nested list
        # where each sublist contains the values of nodes at a particular level in the tree, from left to right
        
        # Input: root = [1,2,3,4,5,6,7]
        # Output: [[1],[2,3],[4,5,6,7]]

        q = deque()
        resList = []

        if root:
            q.append(root)

        while q:
            levelList = []

            for i in range(len(q)):
                node = q.popleft()
                levelList.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            # make sure that levelList is non empty b4 we add
            if levelList:
                resList.append(levelList)

        return resList