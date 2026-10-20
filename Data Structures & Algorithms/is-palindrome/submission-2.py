class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen_arr = []
        for ch in s:
            if ch.isalnum():
                sen_arr.append(ch.lower())

        sen = "".join(sen_arr)

        s_rev = sen[::-1]

        if sen==s_rev:
            return True 
        else:
            return False