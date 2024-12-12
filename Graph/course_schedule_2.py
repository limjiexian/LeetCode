from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ DFS Approach """
        adj_list = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj_list[a].append(b)

        visited = set()
        res = []

        def dfs(curr):
            if curr in visited:
                return False

            if curr in res:
                return True
            
            visited.add(curr)

            for neigh in adj_list[curr]:
                if not dfs(neigh):
                    return False
            
            res.append(curr)
            visited.remove(curr)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []

        
        if len(res) == numCourses:
            return res
        else:
            return []