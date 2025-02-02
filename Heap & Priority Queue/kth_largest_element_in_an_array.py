from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """ Min Heap """
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)

        return heap[0]
