class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        n = len(prices)
        i,j = 0,1
        while j<n:
            if prices[i]>prices[j]:
                i = j
                j = i+1 
                continue 
            profit = max(profit,prices[j]-prices[i]) 
            j += 1 
        return profit