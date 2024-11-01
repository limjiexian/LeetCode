from typing import List


# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         # undirected graph
#         # use parentNode parameter, so that we know if we backtracked to parentNode. this way we know 
#         # it is not a cycle
#         # nodes labeled from 1 to n, means 1-indexed
        
#         # intiially 
#         # no cycles + n-1 edges

#         # afterwards
#         # 1 additional edge is added to the graph
#         # this edge have 2 diff node to choose from
#         # this edge is not an edge that have previously existed in the graph

#         # Goal:
#         # return an edge that can be removed so that the graph is still connected + no cycle 
#         # if multiple answer, only return the edge that appears last in the input edges
#         # i.e. they want us to return the edge that is connected to the more behind de node

#         # edges[i] = [ai, bi]

#         # we wan 1 to n nodes 
#         adj = {i: [] for i in range(1, len(edges) + 1)}

#         for ai, bi in edges:
#             adj[ai].append(bi)
#             adj[bi].append(ai)
        
#         # find the edges that leads to cycle
#         # check these edges, which will not lead to a disconnected graph
#         # return the edges that appear last in the input edges

#         # i think easy way to do this is find all edges that leads to cycle first
#         # then process them to check which one will lead to disconnected graph
#         # then go thru the edges to see which is the one that appear last in edges

        
#         visited = set()
#         curr_path = []
#         candidate = []

#         def backtrack(node, parent):
#             # Base case for cycle detection
#             if node in curr_path:
#                 # Find the start of the cycle in curr_path
#                 node_index = curr_path.index(node)

#                 # Collect all edges in the cycle
#                 for i in range(node_index, len(curr_path) - 1):
#                     candidate.append([curr_path[i], curr_path[i + 1]])
#                 # Add the edge that closes the cycle
#                 candidate.append([curr_path[-1], node])
                
#                 return  # Stop further recursion once cycle is found

#             # Mark the node in current path for cycle tracking
#             curr_path.append(node)

#             # Visit each neighbor
#             for neighbor in adj[node]:
#                 if neighbor == parent:
#                     continue  # Skip backtracking to the parent node
#                 backtrack(neighbor, node)

#             # Backtrack step: remove node from path and mark as visited
#             curr_path.pop()
#             visited.add(node)

#         # Run DFS from each node to detect cycles, prioritizing last-edge order
#         for i in range(1, len(edges) + 1):
#             if i not in visited:
#                 backtrack(i, i)

#         # Determine the last occurring edge in the original input that forms the cycle
#         for edge in reversed(edges):
#             if edge in candidate:
#                 return edge

#         return []

#         # reason why first edge that that caused a cycle we return immediately already is cos
#         # adding edge to a connected graph will always end up in a cycle
#         # cos u are creating a 2nd path
#         # this means first edge will also be the last occuring edge that causes cycle
        

# UnionFind method
# O(n)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges) + 1)

        # [1, 2, 3]: parent
        # [1, 1, 1]: rank

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):
            # for each pair, check which one have higher rank
            # if higher, then that will be the parent else opposite
            # also if both have the same parent already, then we return False

            parentA = find(a)
            parentB = find(b)

            if parentA == parentB:
                return False
            
            if rank[parentA] > rank[parentB]:
                rank[parentA] += rank[parentB]
                parent[parentB] = parentA
            else:
                rank[parentB] += rank[parentA]
                parent[parentA] = parentB

            return True
        
        for a, b in edges:
            if not union(a,b):
                return [a, b]
            














        