class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = [-1]*n

        def fun(ind):
            if ind>=n:
                return 1
            
            if dp[ind] != -1:
                return dp[ind]
            
            if s[ind] == '0':
                return 0
    
            ans = fun(ind+1)
            
            if ind+1 < n and 10 <= int(s[ind:ind+2]) <= 26:
                ans += fun(ind+2)
            
            dp[ind] = ans 
            return ans 
        
        return fun(0)