from typing import List

# Cycle detection using dfs
# Concise steps:
# 1. Initialize adjacency list reqMap for prerequisites.
# 2. Populate adjacency list with each course’s prerequisites.
# 3. Define backtrack function:
# -- If course is in visited, return True.
# -- If course is in currentPath, return False (cycle detected).
# -- Add course to currentPath.
# -- Recursively check all prerequisites; if any return False, stop and return False.
# -- Remove course from currentPath after processing.
# 4. Run backtrack on each course:
# -- If backtrack(course) is False, return False.
# -- Otherwise, add course to visited.
# 5. Return True if all courses can be completed without cycles.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prequisties [0, 1] == must take course 1 first, if you want to take course 0
        # numCourses = total # of courses required to take

        # map courses to their prerequisites
        reqMap = {}

        for i in range(numCourses):
            reqMap[i] = []

        for pair in prerequisites:
            reqMap[pair[0]].append(pair[1]) 
    
        visited = set() # if visited means this course is definitely possible to take
        currentPath = set() # path we traversed already when we are checking for any cycle in the prequisites for a specific course

        def backtrack(course):
            # base case
            if course in visited:
                return True

            if course in currentPath:
                return False

            currentPath.add(course)

            for c in reqMap[course]:
                if not backtrack(c):
                    return False
                    
            currentPath.remove(course)

            return True
        
        for course in range(numCourses):
            if not (backtrack(course)):
                return False
            else:
                visited.add(course)
        
        return True

        
# Topological sort method
# Concise steps
# - Initialize indegree and adjacency list.
# - Populate indegree and adjacency list using prerequisites.
# - Enqueue courses with indegree 0.
# - Process queue with BFS:
# - For each dequeued course, decrement indegree of dependents and enqueue any with indegree 0.
# - Return finish == numCourses to check if all courses are completed.

"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Initialize indegree array and adjacency list
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        
        # Step 2: Populate indegree and adjacency list based on prerequisites
        for src, dst in prerequisites:
            indegree[dst] += 1
            adj[src].append(dst)

        # Step 3: Initialize queue with courses having no prerequisites
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        
        # Step 4: Process courses in topological order
        finish = 0
        while q:
            # Take course with no prerequisites
            node = q.popleft()
            finish += 1
            
            # Reduce indegree for dependent courses and add to queue if indegree is zero
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                
        # Step 5: Check if all courses can be completed
        return finish == numCourses
"""