from collections import deque
import heapq
from typing import Counter, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # specialized dictionary that counts the freq for each element in tasks
        # end result is basically dictionary key: freq
        # e.g. the object will look like -> Counter({'A': 2, 'B': 1, 'C': 1})
        count = Counter(tasks)

        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        q = deque()
        time = 0 

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                
                if cnt != 0:
                    q.append([cnt, time+n])

            if q and q[0][1] == time:
                item = q.popleft()
                heapq.heappush(maxHeap, item[0])            
                
        return time

        # time complexity analysis:
        # t = # of unique task
        # heapifying maxHeap will take O(t) time

        # while loop:
        # n = number of tasks
        # heappush and heappop will each take log t time. and since the loop will run for n time, total time will be o(n log t)

        # deque takes O(1) time for each operation so we dont count this as it is trivial

        # final time complexity = O(t + n log t)


        # space complexity analysis
        # O(t) space for the maxHeap
        # O(n) space for the deque

        # final space complexity = O(t + n)
