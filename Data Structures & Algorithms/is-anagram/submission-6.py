class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        cunt_s = {}
        cunt_t = {}
        for i in range(len(s)):
            cunt_s[s[i]] = cunt_s.get(s[i],0)+1
            cunt_t[t[i]] = cunt_t.get(t[i],0)+1
        
        for k,v in cunt_s.items():
            if k not in cunt_t or cunt_t[k] != v:
                return False 
        return True