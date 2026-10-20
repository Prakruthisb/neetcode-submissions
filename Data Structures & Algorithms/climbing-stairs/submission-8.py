class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        dp[0] = 1

        def fun(ind):
            if ind < 0:
                return 0 
            if dp[ind] != -1:
                return dp[ind]
            dp[ind] = fun(ind-1)+fun(ind-2)
            return dp[ind]
        
        return fun(n)