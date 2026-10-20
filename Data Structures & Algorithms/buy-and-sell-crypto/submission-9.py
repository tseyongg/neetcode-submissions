class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        l, r = 0, 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r += 1
            else:
                best = max(best, profit)
                r += 1
        return best