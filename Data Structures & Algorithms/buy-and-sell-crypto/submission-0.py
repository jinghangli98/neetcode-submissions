class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_profit = 0
        for current_price in prices:
            current_profit = current_price - min_price
            if current_profit > max_profit:
                max_profit = current_profit

            if current_price < min_price:
                min_price = current_price
        
        return max_profit