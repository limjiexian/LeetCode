from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = {i: [] for i in range(n)}

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, prev_node):
            # cycle detected
            if node in visited:
                return False

            visited.add(node)
            
            for child in adj[node]:
                if child != prev_node:
                    if not dfs(child, node):
                        return False

            return True
        
        if not dfs(0, -1):
            return False

        return True if len(visited) == n else False
        
        
# 0: 1, 2, 3
# 1: 4
# 2: 1
# 3: 1