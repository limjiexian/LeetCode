from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Given:
            - coins -> represent diff denominations
            - amount -> target amount of money
        
        Task
            - return -> fewest num of coins that sum to target amount
            - return -1 if impossible to reach target amount
        
        - unlimited usage of each coin
        """
        
        """ DFS Brute Force """
        # def dfs(total, count):
        #     # base case
        #     if total == amount:
        #         return count

        #     minCount = 1e7
        #     for coin in coins:
        #         if coin + total <= amount:
        #             minCount = min(minCount, dfs(coin + total, count + 1))

        #     return minCount

        # return dfs(0, 0) if dfs(0,0) != 1e7 else -1

        """ DFS with Cache """
        # memo = {}

        # if amount == 0:
        #     return 0

        # def dfs(total):
        #     # base case
        #     if total == amount:
        #         return 0

        #     if total in memo:
        #         return memo[total]

        #     res = 1e9
        #     for coin in coins:
        #         if coin + total <= amount:
        #             res = min(res, 1 + dfs(coin + total))
            
        #     memo[total] = res

        #     return memo[total]

        # sol = dfs(0)

        # return -1 if sol == 1e9 else sol

        """ Iterative Bottom up """
        dp = [1e9] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            res = 1e9
            for coin in coins:
                if i - coin >= 0:
                    res = min(res, dp[i-coin] + 1)

            dp[i] = res    

        return -1 if dp[amount] == 1e9 else dp[amount]














