class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in d:
                d[sorted_str] = [s]
            else:
                d[sorted_str].append(s)

        ans = []
        for key,value in d.items():
            ans.append(value)
        return ans    