class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        l = float('inf')
        n = len(s)

        for i in range(n):
            h = {}
            for ch in t:
                h[ch] = h.get(ch,0)+1
            cunt = 0
            for j in range(i,n):
                if s[j] in h and h[s[j]] > 0:
                    cunt += 1 
                h[s[j]] = h.get(s[j],-1) - 1
                if cunt == len(t):
                    sub_str = s[i:j+1]
                    if len(sub_str) < l:
                        ans = sub_str
                        l = len(sub_str)
                    break
        return ans