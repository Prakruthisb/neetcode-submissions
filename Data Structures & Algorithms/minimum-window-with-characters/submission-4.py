class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        len_ans = float('inf')
        n = len(s)

        l,r = 0,0
        cunt = 0 
        h = {}
        for ch in t:
            h[ch] = h.get(ch,0)+1
        while r<n:
            if s[r] in h and h[s[r]] > 0:
                cunt += 1 
            h[s[r]] = h.get(s[r],-1) - 1

            if cunt == len(t):
                while l<=r:
                    sub_str = s[l:r+1]
                    if len(sub_str) < len_ans:
                        ans = sub_str
                        len_ans = len(sub_str)
                    h[s[l]] += 1
                    if h[s[l]] == 1:
                        cunt -= 1 
                        l+=1
                        break 
                    l+=1
            r += 1
        return ans
            