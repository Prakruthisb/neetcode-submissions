class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+1)
        def fun(n):
            if n<=1:
                return 1 
            if dp[n] != -1:
                return dp[n]
            dp[n] = fun(n-1) + fun(n-2)
            return dp[n] 
        
        return fun(n)