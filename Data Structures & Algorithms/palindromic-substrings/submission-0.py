class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def is_palindrome(s):
            return s == s[::-1]

        n = len(s) 
        
        for i in range(n):
            for j in range(i,n):
                if is_palindrome(s[i:j+1]):
                    ans += 1 
        
        return ans 