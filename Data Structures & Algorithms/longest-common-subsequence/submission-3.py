class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [[-1]*n2 for _ in range(n1)]
        
        def fun(ind1,ind2):
            if ind1 < 0 or ind2 < 0:
                return 0 
            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]
            if text1[ind1] == text2[ind2]:
                dp[ind1][ind2] = 1 + fun(ind1-1,ind2-1)
                return dp[ind1][ind2]
            dp[ind1][ind2] = max(fun(ind1,ind2-1),fun(ind1-1,ind2))
            return dp[ind1][ind2]

        return fun(n1-1,n2-1)