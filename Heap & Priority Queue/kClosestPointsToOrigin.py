import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Given 2-D arrray -> represent coordinates of a point on x-y axis
        # Given integer k
        # Goal: 
        # - return k closest points to the origin (0,0)
        # The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
        # result = math.sqrt()
        # but actually dont need to do .sqrt() because sqrt 5 will still be bigger than sqrt 4, so just save the b4 sqrt value will do
        
        
        # get the dist
        dist = []

        for x, y in points:
            d = (x ** 2) + (y ** 2)
            dist.append([d, x, y])  # we can do this because later we heapify, they will order them, by the first element, e.g. d

        heapq.heapify(dist)

        res = []
        for i in range(k):
            item = heapq.heappop(dist)
            res.append([item[1], item[2]])
        
        return res

        # time complexity:
        # O(n) to heapify
        # we will pop k times. and each heappop takes log n time, combine = O(k log n)
        # therefore total time complexity = O(n + k log n)

        # space complexity:
        # O(n) for the heap

        # Heap-based approach (O(n + k log n)) is generally better when k is small because you avoid sorting the entire list. Sorting is O(n log n), which is more expensive when you only need k closest points.
        # In the heap-based approach, you don't need to sort the entire list. Instead, you're building a heap to maintain only the k closest points (or the largest distances when using a max heap for the closest points).
        
        # Array-based approach
        # sorting takes n log n time
        # (O(n log n)) is beneficial when k is large or close to n. In such cases, both approaches perform similarly.