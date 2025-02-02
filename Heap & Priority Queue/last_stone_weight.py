import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        # create max heap
        for stone in stones:
            heapq.heappush(heap, stone * - 1)
        
        # loop and pop the 2 heaviest stones
        while len(heap) > 1:
            x = heapq.heappop(heap) * -1
            y = heapq.heappop(heap) * -1

            if x == y:
                continue
            elif x < y:
                new_weight = y - x
            else:
                new_weight = x - y
            
            heapq.heappush(heap, new_weight * - 1)
        
        return heap[0] * -1 if heap else 0

        

