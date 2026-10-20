class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            if not s[i].isalnum():
                s = s.replace(s[i]," ")

        s = s.lower().replace(" ","")

        s_rev = s[::-1]

        if s==s_rev:
            return True 
        else:
            return False