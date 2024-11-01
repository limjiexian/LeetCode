from typing import List


# JX Top down method
# BAD METHOD, I BASICALLY RECALCULATING MY SUBPROBLEM, which is dumb LOL
# class Solution:

#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         # cost array -> cost[i] tells us how much it takes to take a step from ith floor 
#         # we can step to either i+1 or i+2 floor after paying
#         # we can choose to start at index 0 or index 1 floor

#         # Goal
#         # - return min cost to reach the top of the stairs

        
#         # find the min cost to reach each floor
#         # as we can take either 1 step or 2 steps
#         # so we need see between floor 0 or floor 1 which floor is cheaper to go to floor 2
#         # calculate the min cos to reach floor 2, then shift one and two to the right by 1
#         one = 0
#         two = 0

#         i, j = -1, 0

#         while j < len(cost) - 1:
#             if i == -1:
#                 third = min(one, (cost[j] + two))
#             else:
#                 third = min((cost[i] + one), (cost[j] + two))

#             temp = two
#             two = third
#             one = temp              

#             i += 1
#             j += 1
        
#         return min((cost[i] + one), (cost[j] + two))


# Neetcode Bottom up method


        

        