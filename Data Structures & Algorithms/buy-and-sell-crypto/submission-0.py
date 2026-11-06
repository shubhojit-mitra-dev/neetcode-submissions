class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for price in prices:
            curr = price - min_buy
            max_profit = max(curr, max_profit)
            min_buy = min(price, min_buy)

        return max_profit