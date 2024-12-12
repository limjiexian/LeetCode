# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Given:
        - a node in connected undirected graph
        - node values -> 1 to n
        - n = total number of nodes
        - input node is always node = 1

        Task:
        - return a deep copy of the graph

        """

        """ BFS """
        # clone node then add to queue
        # for each node in queue
            # we check its neighbors whether it has been cloned. if never we clone them then add to queue
            # then we append the cloned neighbors it to the node

        # old_2_new = {}
        
        # if node == None:
        #     return None

        # old_2_new[node] = Node(node.val)
        # q = deque()
        # q.append(node)

        # while q:
        #     size = len(q)

        #     while size > 0:
        #         curr = q.popleft()

        #         for child in curr.neighbors:
        #             if child not in old_2_new:
        #                 old_2_new[child] = Node(child.val)
        #                 q.append(child)
            
        #             old_2_new[curr].neighbors.append(old_2_new[child])
                    
        #         size -= 1
            
        
        # return old_2_new[node]

        # 2: 1, 3
        # 1: 2
        # 3: 2

        """ DFS """

        visited = set()
        old_2_new = {}

        if node == None:
            return None

        def dfs(curr):
            if curr in visited:
                return

            old_2_new[curr] = Node(curr.val)
            visited.add(curr)
            
            for child in curr.neighbors:
                dfs(child)
                old_2_new[curr].neighbors.append(old_2_new[child])

            return

        dfs(node)

        return old_2_new[node]










        
        