# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Given:
        # root of a binary tree
        # Goal:
        # return only values of the nodes that are visible from right side of the tree, ordered from top to bottom
        
        # i think basically is just the right most nodes, as these are the only one that can be seen from the right side
        # so for each level we want to find the right most nodes
        # since they are us to order them from top to bottom, i think bfs is the play here

        # but how do we know which is the right most node
        # for each level the right most node of a binary tree will be the largest node value 
        
        # WRONGGGGG because they didnt say this is a BST therefore wont have BST properties.
        # CORRECT METHOD: we can just get the last node that was being poped out of the deque for each level, as that will be our right most node

        q = deque()

        if root:
            q.append(root)

        res = []

        while q:
            targetNode = -999
            for i in range(len(q)):
                node = q.popleft()
                targetNode = node.val

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
            if targetNode != -999:
                res.append(targetNode)

        return res






