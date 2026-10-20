class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""

        n = len(s)

        def fun(l,r):
            nonlocal ans
            while l>=0 and r < n:
                if s[l] == s[r]:
                    sub_str = s[l:r+1]
                    if len(sub_str) > len(ans):
                        ans = sub_str
                    l-=1 
                    r+=1
                else:
                    break

        for i in range(n):
            fun(i,i)
            fun(i,i+1)

        return ans 