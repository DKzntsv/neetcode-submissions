class Solution:
    def maxProfit(self, prices: int):
        min_index = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[min_index]:
                min_index = i
            if (prices[i] - prices[min_index]) > max_profit:
                max_profit = prices[i] - prices[min_index]
            
        return max_profit