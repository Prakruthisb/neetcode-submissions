class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        n = len(strs)
        for i in range(n):
            cunt = [0] * 26
            for ch in strs[i]:
                cunt[ord(ch)-ord('a')] += 1 
            d[tuple(cunt)].append(strs[i])
        return list(d.values())