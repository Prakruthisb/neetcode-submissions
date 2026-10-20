class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            ch_set = set()
            for j in range(i,n):
                if s[j] in ch_set:
                    break
                else:
                    ch_set.add(s[j])
            ans = max(ans,len(ch_set))
        return ans