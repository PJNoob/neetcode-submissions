class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float("infinity")
        
        for price in prices:
            buy = min(buy, price)
            profit = max(profit, price - buy)

        return profit