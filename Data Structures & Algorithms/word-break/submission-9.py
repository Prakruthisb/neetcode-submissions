class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) 
        wordDict = set(wordDict)
        dp = [None]*n

        def f(ind):
            if ind>=n:
                return True 
            if dp[ind] is not None:
                return dp[ind]
            for i in range(ind,n):
                sub_str = s[ind:i+1]
                if sub_str in wordDict:
                    if f(i+1):
                        dp[ind] = True 
                        return True 
            dp[ind] = False 
            return False 
        
        return f(0)