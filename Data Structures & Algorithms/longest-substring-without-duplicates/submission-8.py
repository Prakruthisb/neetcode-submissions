class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        ch_set = set()
        l,r = 0,0
        while r<n:
            while s[r] in ch_set and l<n:
                ch_set.remove(s[l])
                l += 1 
            ans = max(ans,r-l+1)
            ch_set.add(s[r])
            r += 1
        return ans