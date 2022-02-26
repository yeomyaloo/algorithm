class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_price = 0
        for i in range(len(prices)):
            if i == 0:
                min_price = prices[i]
                pass
            min_price = min(min_price, prices[i])
            max_price = max(prices[i] - min_price, max_price)

        return max_price