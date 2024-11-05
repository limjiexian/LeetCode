from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins -> integer array coins representing coins of diff denominations
        # amount -> our target amount of money to hit

        # Goal
        # - return fewest number of coins needed to hit target amount
        # - return -1 if not possible to hit target amount

        # optimization problem
        # so highly likely a dynamic programming question

        # lets try to solve it brute force way using dfs first
        # If we are allowed to keep choose from e.g. this case 5 choice, unlimited amount of times
        # - always just use for loop, to recursively call the dfs
        
        # def backtrack(amount):
        #     # base case
        #     if amount == 0:
        #         return 0

        #     res = 1e9
            
        #     # main
        #     for coin in coins:
        #         if (amount - coin) >= 0: 
        #             res = min(res, 1 + backtrack(amount-coin))
        #     return res
        
        # minCount = backtrack(amount)

        # if minCount >= 1e9:
        #     return -1
        # else:
        #     return minCount

        # TOP DOWN
        # now that we have the backtracking solution lets try to incoporate cache into it
        # only save into dp[amount] if we found the minCount for said amount

        """
        Time complexity == O(n*t)
        Recursive Calls and Memoization:
        Each unique subproblem (for each amount from 0 to amount) is computed only once due to memoization. So, there are O(amount) unique states that need to be calculated.
        Loop Over Coins:
        For each state (each amount), the algorithm loops through all coins to determine the minimum count of coins needed.
        Let n be the number of coins. For each recursive call, the for loop iterates through n coins, giving O(n) work per state.

        Space Complexity == O(amount) + O(amount) = O(amount)
        Recursion stack will be at worst O(amount)
        - this is because worst case you only have coin=1, so can only reduce amount by 1 for each recursion
        - aka u will need do O(amount) of recursion 

        dict storage of O(amount)
        - as we only store results from 0 to amount
        """
        # dp = {i: -1 for i in range(amount+1)}

        # if amount == 0:
        #     return 0

        # def backtrack(amount):
        #     if dp[amount] != -1:
        #         return dp[amount]
            
        #     if amount == 0:
        #         return 0
            
        #     res = 1e9
        #     for coin in coins:
        #         if amount-coin >= 0:
        #             res = min(res, backtrack(amount-coin) + 1)
            
        #     dp[amount] = res
            
        #     return res
        
        # backtrack(amount)

        # if dp[amount] == 1e9:
        #     return -1
        # else:
        #     return dp[amount]


        # BOTTOM UP
        # normally for bottom up we need to ditch dfs, and just solve it iteratively

        dp = [1e9] * (amount + 1)
        dp[0] = 0

        res = 1e9
        for a in range(1, amount + 1):
            for c in coins:
                if a-c >= 0:
                    dp[a] = min(dp[a], dp[a-c]+1)

        return dp[amount] if dp[amount] != 1e9 else -1



                


            
        

