from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        """ DFS Method """
        # directed graph -> if visited means we got cycle

        adj = {i: [] for i in range(numCourses)}

        for pre in prerequisites:
            a = pre[0]
            b = pre[1]

            adj[a].append(b)

        visited = set()

        def dfs(curr):
            if curr in visited:
                return False

            visited.add(curr)

            for neigh in adj[curr]:
                if not dfs(neigh):
                    return False
            
            visited.remove(curr)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
    
        return True
        
        