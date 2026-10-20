class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            a = [0]*26
            for ch in s:
                a[ord(ch)-ord('a')] += 1 
            if tuple(a) not in d:
                d[tuple(a)] = [s]
            else:
                d[tuple(a)].append(s)

        return list(d.values())