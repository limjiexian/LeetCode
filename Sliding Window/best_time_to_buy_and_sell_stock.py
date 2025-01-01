from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """ Brute Force """
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         buy = prices[i]
        #         sell = prices[j]

        #         profit = sell - buy
                
        #         max_profit = max(max_profit, profit)
        
        # return max_profit

        """ Sliding Window """
        
        if len(prices) == 1:
            return 0
        
        buy_ptr, sell_ptr = 0, 0
        max_profit = 0
        while sell_ptr < len(prices):
            buy = prices[buy_ptr]
            sell = prices[sell_ptr]
            
            if buy > sell:
                buy_ptr = sell_ptr
                sell_ptr += 1
            else:
                profit = sell - buy
                max_profit = max(max_profit, profit)
                sell_ptr += 1
            
        return max_profit

