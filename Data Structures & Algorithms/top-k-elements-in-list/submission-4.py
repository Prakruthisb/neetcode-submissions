class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        d = dict(sorted(d.items(),key=lambda x:x[1],reverse=True))
        ans = list(d.keys())
        if len(ans) < k:
            return []
        return ans[:k]