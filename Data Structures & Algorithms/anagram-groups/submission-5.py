class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        n = len(strs)
        for i in range(n):
            cunt = Counter(strs[i])
            d[tuple(sorted(cunt.items()))].append(strs[i])
        return list(d.values())