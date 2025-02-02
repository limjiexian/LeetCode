from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # undirected graph with n nodes
        # edges array # edges[i] = [a, b]

        # 1st Attempt thought process:
        # populate the adj list
        # for each node that has not been visited
        # apply dfs on them, this dfs will recursively run until we reach the end of the connection
        # if we cant proceed any further means we have explored all the nodes in this subgraph
        # then we increment # of subgraph count 

        # {key_expression: value_expression for item in iterable if condition}
        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()

        def backtrack(node):
            # base case
            if node in visited:
                return
            
            visited.add(node)

            for edge in adj[node]:
                backtrack(edge)

            return
        
        count = 0
        for i in range(n):
            if i not in visited:
                backtrack(i)
                count += 1

        return count

        """ Union Find version """
        # def find(x):
        #     if parent[x] != x:
        #         parent[x] = find(parent[x])    
        
        #     return parent[x]
        
        # def union(x, y):
        #     px, py = find(x), find(y)

        #     if px == py:
        #         return False
        #     elif rank[px] > rank[py]:
        #         # px eat py
        #         parent[py] = px
        #         rank[px] += rank[py]
        #     else:
        #         parent[px] = py
        #         rank[py] += rank[px]

        #     return True
        
        # parent = [i for i in range(n)]
        # rank = [1] * n

        # for e1, e2 in edges:
        #     union(e1, e2)
            
        # visited = set()
        # for i in range(n):
        #     root = find(i)

        #     if root not in visited:
        #         visited.add(root)

        # return len(visited)
        
        






        