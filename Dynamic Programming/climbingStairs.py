class Solution:
    def climbStairs(self, n: int) -> int:
        
        # number of choice at n step is 1
        # because you chose to stay

        # number of choice at n-1 step (in order to go our target n=5) is, 
        # e.g. n=5 and we are at 4, we only got 1 choice, that is to take 1 step
        one, two = 1, 1

        # Base Case Initialization: Starting with one = 1 and two = 1 already accounts for the first two steps.
        # Loop Iteration: Each loop iteration simulates reaching a new step using the previous two steps. 
        # Since we already set the base cases, we need n - 1 iterations to reach the n-th step.

        # i.e. since we want one to end at n=0 position
        # and that our one started at n-1 position
        # means we only need to move one to the left by n-1 times then we reach our n=0
        
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        
        return one

        # time complexity O(n) time
        # space complexity O(1)