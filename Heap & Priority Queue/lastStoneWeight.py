import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # given an array of integers stones
        # stones[i] represent the weight of ith stone
        # Goal:
        # - smash the 2 hoeaviest stones
        # - if x == y, both destroyed
        # - if x < y, x destroyed, and y get new weight = y - x
        # keep run the above until only one stone remains
        # return weight of last stone, or return 0 if none remain

        # use heap to maintain the list
        # pop 2 to get the 2 heaviest one and fight then push the results
        
        maxHeap = []
        # maxHeap
        for stone in stones:
            heapq.heappush(maxHeap, -1 * stone)

        while len(maxHeap) > 1:
            x = -1 * heapq.heappop(maxHeap)
            y = -1 * heapq.heappop(maxHeap)

            if x == y:
                continue
            elif x < y:
                y = y - x
                y = -1 * y
                heapq.heappush(maxHeap, y)
            else:
                x = x - y
                x = -1 * x
                heapq.heappush(maxHeap, x)
        

        return (-1 * maxHeap[0]) if maxHeap else 0
        
#         -2
#         -3
#         -6
#         -2
#         -4

# -6, -4, -3, -2, -2

# -3, -2, -2, -2 

# -2, -2, -1


# time complexity: 
# O(n log n) for heappush [each heappush is log n]
# O(n log n) for the while loop as worst case u smash 1 stone each iteration, so heappop + heappush = O(logn) + O(logn) = O(log n). And cos u need do n-1 times aka n * log n
# space complexity: O(n) as heap is usually a binary tree stored in array/list

        
