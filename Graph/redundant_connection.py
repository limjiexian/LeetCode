from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """ DFS Optimal """

        # adj = {i: [] for i in range(len(edges)+1)}

        # for e1, e2 in edges:
        #     adj[e1].append(e2)
        #     adj[e2].append(e1)

        # cycle = {}

        # def dfs(curr, prev):
        #     if curr in cycle:
        #         for node in cycle.keys():
        #             if node == curr:
        #                 return True

        #             del adj[node]
        #         return True
            
        #     cycle[curr] = None

        #     for neigh in adj[curr]:
        #         if neigh != prev and dfs(neigh, curr):
        #             return True
                
        #     del cycle[curr]
        
        #     return False

        # dfs(edges[0][0], -1)

        # for e1, e2 in reversed(edges):
        #     if e1 in cycle and e2 in cycle:
        #         return [e1, e2]

        """ DFS Optimal without the cycle.keys() loop """

        # adj = {i: [] for i in range(len(edges)+1)}

        # for e1, e2 in edges:
        #     adj[e1].append(e2)
        #     adj[e2].append(e1)

        # cycle = set()

        # def dfs(curr, prev):
        #     if curr in cycle:
        #         return True
            
        #     cycle.add(curr)

        #     for neigh in adj[curr]:
        #         if neigh != prev and dfs(neigh, curr):
        #             return True
                
        #     cycle.remove(curr)
        
        #     return False

        # dfs(edges[0][0], -1)

        # for e1, e2 in reversed(edges):
        #     if e1 in cycle and e2 in cycle:
        #         return [e1, e2]


        """ Union Find """
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            p1, p2 = find(x), find(y)

            # found our cycle
            # cos we are trying to join 2 subgraph that has the same parent node
            if p1 == p2:
                return False

            # p1 will absorb p2
            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            
            return True

        n = len(edges)

        # + 1 cos dh node 0, we start from node = 1
        parent = [i for i in range(n+1)]
        rank = [1] * (n + 1)

        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]



