class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Given
        - array of integers -> cost
            - cost[i] -> the cost of taking a step at ith floor
            - after paying the cost -> can choose step +1 or step +2
        - can choose to start from index 0 or index 1

        Task
        - return min cost to reach the top of the staircase (go beyond the last index in cost)

        """
        
        """ DFS BruteForce """
        # n = len(cost)-1

        # def dfs(i, total):
        #     # base case
        #     if i > n:
        #         return total

        #     return min(dfs(i+1, total + cost[i]), dfs(i+2, total + cost[i]))
        
        # minCost = min(dfs(0, 0), dfs(1, 0))

        # return minCost

        """ DFS with cache (Top down) """
        # def dfs(i):
        #     # idea is that, our goal is to calculate the min cost to go past the last step of the staircase. If we are already past the last
        #     # step of the stairs, this means there is no additional cost to pay at there as we already completed our climb
        #     if i > len(cost)-1:
        #         return 0

        #     if memo[i] != -1:
        #         return memo[i]
            
        #     memo[i] = min(dfs(i+1) + cost[i], dfs(i+2) + cost[i])

        #     return memo[i]

        # memo = {i: -1 for i in range(len(cost))}
        # dfs(0)
        # return min(memo[0], memo[1])

        """ Iterative Bottom up """
        # # Initialize a DP array with extra space for dp[len(cost)] and dp[len(cost)+1] (both set to 0),
        # # which represent the cost of being beyond the last step.
        # # dp[i] will store the minimum cost to climb to the top starting from step i.
        # # Start filling dp array from the last step toward the first step.
        # # Finally, return the minimum cost to climb to the top starting from either step 0 or step 1.

        # dp = [0] * (len(cost) + 2)  # DP array initialized with 0 for extra steps

        # # Iterate from the last step down to the first step
        # for i in range(len(cost) - 1, -1, -1):
        #     # Minimum cost to climb from step i includes cost[i] and the minimum of
        #     # the costs to climb from the next two steps (i+1 and i+2)
        #     dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        # # Return the minimum cost to climb to the top starting from step 0 or step 1
        # return min(dp[0], dp[1])

        """ Two Pointer """
        # This approach reduces space complexity from O(n) to O(1) by maintaining
        # only two variables (`front` and `back`) to represent dp[i+1] and dp[i+2].
        # Iterate from the last step toward the first step, updating the two pointers as you go.

        front, back = 0, 0  # `front` represents dp[i+1], `back` represents dp[i+2]

        # Iterate from the last step down to the first step
        for i in range(len(cost) - 1, -1, -1):
            # Compute the current step cost using the two pointers
            curr = cost[i] + min(front, back)

            # Shift pointers: Update `front` to the current step cost (`curr`)
            # and move `back` to the previous `front`
            front, back = curr, front

        # Return the minimum cost to climb to the top starting from step 0 or step 1
        return min(front, back)        








        