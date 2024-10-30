from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Given:
        # n nodes labeled from 0 to n-1
        # list of undirected edges, each edge is a pair of nodes
        
        # Definition of valid tree
        # a graph must be connected, i.e. every node must be reachable from any other node
        # must not have cycle

        # Tasks
        # check whether these edges made up a valid tree

        # 1st attempt thought process
        # using the edges given to populate our adjacency list
        # for each node, backtrack all the nodes that are connected to it using the adj list
        # as we backtrack if we found a node that we have already visited while traversing, this means
        # we have a cycle. 
        # after all that is done, we check if for each node, can we reach every other node
        # but i am not sure if we are able to do both checking at the same time

        adj_list = {}

        for i in range(n):
            adj_list[i] = []

        for edge in edges:
            a = edge[0]
            b = edge[1]

            if b not in adj_list[a]:
                adj_list[a].append(b)

            if a not in adj_list[b]:
                adj_list[b].append(a)        

        visited = set()

        def backtrack(node, prevParent):
            # base case
            if node in visited:
                return False
            
            visited.add(node)

            for edge in adj_list[node]:
                if edge == prevParent:
                    continue
                if not backtrack(edge, node):
                    return False
            
            return True
        
        if not backtrack(0, -1) or n != len(visited):
            return False
        else:
            return True

# Code summary:
# 1. **Build adjacency list** from edges to represent the undirected graph.

# 2. **Define `backtrack` function**:
#    - Mark `node` as visited.
#    - Traverse neighbors; if any are visited but not the parent, return `False` (cycle detected).

# 3. **Run `backtrack` from node 0**:
#    - If `backtrack` returns `False` or all nodes weren’t visited, return `False` (not a valid tree).
#    - Otherwise, return `True`.

sol = Solution()

n=5
edges=[[0,1],[0,2],[0,3],[1,4]]

print(sol.validTree(n, edges))












