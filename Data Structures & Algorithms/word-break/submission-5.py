class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [-1]*(n+1)
        dp[n] = True 

        def f(i):
            if dp[i] != -1:
                return dp[i]
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    if f(i+len(word)):
                        dp[i] = True 
                        return True 
            dp[i] = False
            return False
        
        return f(0)