class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            d[num] = d.get(num,0)+1
        
        a = [(v,k) for k,v in d.items()]
        a.sort(key=lambda x:x[0],reverse=True)
        ans = []
        for i in range(k):
            ans.append(a[i][1])
        return ans