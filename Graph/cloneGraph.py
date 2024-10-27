
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Given
        # - a connected undirected graph
        # - each node contains an int value and a ListNode of its neighbors
        # - # of nodes is n
        # - 1-indexed system, aka node 1 = index 1 in the adjacency list

        # definition
        # - adjacency list == a mapping of nodes to list, used to represent finite graph

        # Task
        # - return deep copy of the graph
        
        # Input: adjList = [[2],[1,3],[2]]
        # node = 1 have neighbor of 2
        # node = 2 have neighbors of 1,3    // aka connect to 1 and 3
        # node = 3 have neighbor of 2
        
        # Neetcode version -> DFS method
        # time complexity is O(N + E)
        # N = # of nodes, as you process each node once
        # E = # of edges, as you traverse only the direct edges connected to each node
        # - Each edge is traversed at most twice (once for each connected node).
        # - technically is 2E but cos big O we round to O(E)

        # Space complexity
        # Recursive stack -> the depth of the recursion aka O(N) number of nodes you travel
        # Storage for cloned  Node -> O(N) as u will clone N number of nodes
        # total space complexity == O(N)

        # oldToNew = {}

        # def backtrack(node):
        #     # base case
        #     if node in oldToNew:
        #         return oldToNew[node]
            
        #     copy = Node(node.val)
        #     oldToNew[node] = copy

        #     for neighbor in node.neighbors:
        #         copy.neighbors.append(backtrack(neighbor))

        #     return copy

        # return backtrack(node) if node else None

        # BFS my method

        # Edge case
        if node is None:
            return None

        oldToNew = {}

        q = deque()
        q.append(node)
        copy = Node(node.val)
        oldToNew[node] = copy

        while q:
            curr = q.popleft()

            for n in curr.neighbors:
                if n not in oldToNew:
                    copy = Node(n.val)
                    oldToNew[n] = copy
                    q.append(n)
            
                oldToNew[curr].neighbors.append(oldToNew[n])

        return oldToNew[node]
        


