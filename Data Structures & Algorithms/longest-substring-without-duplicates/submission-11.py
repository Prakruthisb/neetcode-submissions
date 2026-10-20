from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        ch_dict = defaultdict(int)
        l,r = 0,0
        while r<n:
            if s[r] in ch_dict:
                l = max(l,ch_dict[s[r]] + 1)
            ans = max(ans,r-l+1)
            ch_dict[s[r]] = r
            r += 1
        return ans