class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            profit = prices[sell] - prices[buy]
            if profit < 0:
                buy = sell
            else:
                max_profit = max(max_profit, profit)
            sell += 1
        return max_profit
                    
            