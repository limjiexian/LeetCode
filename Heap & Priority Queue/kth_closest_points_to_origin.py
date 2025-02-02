import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ Using Min Heap -> Neetcode"""
        # x1, y1 = 0, 0
        # dist = []

        # for x2, y2 in points:
        #     # x2, y2 = point[0], point[1]

        #     d = math.sqrt((x1-x2)**2  + (y1-y2)**2)
        #     dist.append([d, x2, y2])

        # heapq.heapify(dist)

        # res = []
        # for i in range(k):
        #     item = heapq.heappop(dist)

        #     res.append([item[1], item[2]])
        
        # return res

        """ Using Max Heap"""
        
        x1, y1 = 0, 0

        dist = []

        for x2, y2 in points:
            d = (x1-x2)**2 + (y1-y2)**2

            if len(dist) < k:
                heapq.heappush(dist, [d * -1, x2, y2])
            else:
                heapq.heappushpop(dist, [d * -1, x2, y2])
        
        res = []

        for item in dist:
            d, x2, y2 = item
            res.append([x2, y2])

        return res
