class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range (len(prices)):
            for j in range (i+1, len(prices)):
                # if prices[j] - prices[i] > 0:
                    # profit = 0
                    # append.profit()
                    # res = max(profit)
                profit = prices[j] - prices[i]
                res = max(res, profit)

        return res