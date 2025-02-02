import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums

        heapq.heapify(self.heap)

        for i in range(len(self.heap)-k):
            heapq.heappop(self.heap)


    def add(self, val: int) -> int:
        # now we have k+1 elements
        heapq.heappush(self.heap, val)

        # if we only have element less than k, we dont want to pop it
        if len(self.heap) > self.k:
            # remove the kth + 1 th element
            heapq.heappop(self.heap)

        # return min value from our heap     
        return self.heap[0]

        
        
        
