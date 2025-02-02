from collections import deque
import heapq
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        max_heap = []
        freq_counter = [0] * 26
    
        for task in tasks:
            freq_counter[ord(task) - ord("A")] += 1
        
        print("freq_counter = ", freq_counter)
        
        for freq in freq_counter:
            if freq == 0:
                continue
    
            heapq.heappush(max_heap, freq * -1)

        
        print("max_heap = ", max_heap)

        q = deque() # [task_freq, task_cycle]
        cycle = 0

        while True:
            if not q and not max_heap:
                return cycle
            
            if q and q[0][1] == cycle:
                print("yo")
                task_freq, task_cycle = q.popleft()
                heapq.heappush(max_heap, task_freq)
            
            if max_heap:
                task_freq = heapq.heappop(max_heap)
                task_freq += 1

                if task_freq < 0:
                    q.append([task_freq, cycle + n + 1])
            
            cycle += 1



