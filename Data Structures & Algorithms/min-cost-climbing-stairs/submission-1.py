class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1]*n

        def fun(ind):
            if ind>=n:
                return 0 
            if dp[ind] != -1:
                return dp[ind]
            a = cost[ind]+fun(ind+1)
            b = cost[ind]+fun(ind+2)
            dp[ind] = min(a,b)
            return dp[ind]
        
        fun(0)
        fun(1)
        return min(dp[0],dp[1])