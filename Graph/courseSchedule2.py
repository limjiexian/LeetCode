class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prerequisites[i] = [a, b] : means must take b in order to take a

        # Goal 
        # return a valid ordering of courses you can take to finish all the courses
        # if got more than 1 valid ans, return any of them will do
        # else if not possible to finish the course return empty array
        # - aka got cycle in this directed graph

        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[a].append(b)

        visited = set()
        current_path = set()

        visitedOrder = set()
        order = []
        
        def backtrack(node, parentNode):
            # base case
            if node in visited:
                return True
            
            if node in current_path:
                return False

            current_path.add(node)

            # main recursive
            for neigh in adj[node]:
                if not backtrack(neigh, node):
                    return False
                if neigh not in visitedOrder:
                    order.append(neigh)
                    visitedOrder.add(neigh)
            
            current_path.remove(node)
        
            return True

            
        for course in range(numCourses):
            if not backtrack(course, course):
                return []
            visited.add(course)
            if course not in visitedOrder:
                order.append(course)
                visitedOrder.add(course)
        
        if len(visited) != numCourses:
            return []
        else:
            return order

# 0 : 1,2,3
# 1: 4
# 2: 5

        

