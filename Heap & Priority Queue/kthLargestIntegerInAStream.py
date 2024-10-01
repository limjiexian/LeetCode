
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        while self.k < len(self.minHeap):
            heapq.heappop(self.minHeap)
             
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        
        if self.k < len(self.minHeap):
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]

# Time complexity: 
# Constructor: 
# - Heapify: O(n)
# - Popping elements: heappop takes O(log n), we have n-k elements to pop therefore -> O(n-k log n)
# - combine them ans: O(n + (n-k) log n)

# add method:
# - heappush: O(log k) # since heap size is k, therefore log k to insert
# - heappop: O(log k)
# - minHeap[0] is basically like accessing array so O(1)
# - Total ans: O(log k + 1) = O(log k)
        
""" 
Key functions in heapq:

heapq.heappush(heap, item):
Adds a new item to the heap, maintaining the heap property.
Time complexity: O(log n).

heapq.heappop(heap):
Removes and returns the smallest item from the heap, maintaining the heap property.
Time complexity: O(log n).

heapq.heappushpop(heap, item):
Pushes a new item and pops the smallest item in a single operation, ensuring efficiency.
Time complexity: O(log n).

heapq.heapify(iterable):
Converts a list into a heap in-place.
Time complexity: O(n).
"""