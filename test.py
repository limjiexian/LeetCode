from typing import List


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
       
       # Brute Force
        # def dfs(i, total):      
        #     if i >= len(cost):
        #         return total

        #     # 1 step
        #     minCost = dfs(i+1, total + cost[i])

        #     # 2 steps
        #     minCost = min(minCost, dfs(i+2, total + cost[i]))

        #     return minCost

        # return min(dfs(0, 0), dfs(1, 0))

        # print(dfs(0, 0))
        # print(dfs(1, 0))

        # Cache
        memo = {}

        def dfs(i, total):
            if i >= len(cost):
                return total
            
            if i in memo:
                return memo[i]
            
            m1 = dfs(i+1, total + cost[i])
            m2 = dfs(i+2, total + cost[i])
            memo[i] = min(m1, m2)

            return memo[i]


        dfs(0, 0)

        sol = memo[0]

        print(memo[0])
        
        # memo = {}
        
        # dfs(1, 0)

        # sol = min(sol, memo[1])

        # return sol


cost=[1,2,1,2,1,1,1]

s = Solution()

s.minCostClimbingStairs(cost)

