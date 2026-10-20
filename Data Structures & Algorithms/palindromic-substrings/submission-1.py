class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s) 

        def fun(l,r):
            nonlocal ans 
            while l>=0 and r<n:
                if s[l] == s[r]:
                    ans += 1 
                    l -= 1 
                    r += 1 
                else:
                    break
        
        for i in range(n):
            # odd len palindromes 
            fun(i,i)

            # even len palindromes
            fun(i,i+1)
        
        return ans 