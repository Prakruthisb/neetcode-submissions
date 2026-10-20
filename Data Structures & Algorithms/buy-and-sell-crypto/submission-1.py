class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)

        l,r = 0,1
        while r<n:
            if prices[l] < prices[r]:
                profit = max(profit,prices[r]-prices[l])
                r += 1
            elif prices[l] > prices[r]:
                l = r 
                r += 1
            else:
                r += 1
        return profit