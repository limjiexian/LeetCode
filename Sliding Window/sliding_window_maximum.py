from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        """ Monotonic Deque"""
        window = []
        l = 0
        q = deque()
        res = []

        for r in range(len(nums)):
            # maintain our monotonic deque
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # check boundaries
            if q[0] < (r-k+1):
                q.popleft()

            # update max
            if r-k+1 >= 0:
                res.append(nums[q[0]])
        
        return res                
        