class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = float('inf')
        max_profit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            profit = price - lowest

            max_profit = max(profit, max_profit)
        
        return max_profit