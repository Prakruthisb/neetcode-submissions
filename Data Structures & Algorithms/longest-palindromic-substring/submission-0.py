class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""

        def ispalindrome(string):
            return string == string[::-1]

        for i in range(n):
            for j in range(i,n):
                substring = s[i:j+1]
                if ispalindrome(substring) and len(substring) > len(ans):
                    ans = substring 
        
        return ans 