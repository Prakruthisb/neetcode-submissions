class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i,j = 0,n-1

        while i<=j:
            if not s[i].isalnum():
                i += 1 
            elif not s[j].isalnum():
                j -= 1 
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i+=1 
                j-=1
        return True 