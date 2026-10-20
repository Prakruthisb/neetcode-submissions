class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = {}
        dt = {}

        for i in range(len(s)):
            ds[s[i]] = ds.get(s[i],0)+1
            dt[t[i]] = dt.get(t[i],0)+1

        for key in ds.keys():
            if key not in dt or ds[key] != dt[key]:
                return False 
        return True 