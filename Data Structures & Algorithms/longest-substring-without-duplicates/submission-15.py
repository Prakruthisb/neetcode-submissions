class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        i,j = 0,0
        d = {} #ch -> index
        while j<n:
            if s[j] in d:
                i = max(i,d[s[j]]+1)
            ans = max(ans,j-i+1)
            d[s[j]] = j
            j += 1 
        return ans