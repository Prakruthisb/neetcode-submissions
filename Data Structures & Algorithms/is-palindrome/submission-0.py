class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            if not s[i].isalnum():
                s = s.replace(s[i]," ")

        s = s.lower().replace(" ","")

        n = len(s)
        i,j = 0,n-1
        while i<=j:
            if s[i] != s[j]:
                return False 
            else:
                i += 1 
                j -= 1 
        return True 