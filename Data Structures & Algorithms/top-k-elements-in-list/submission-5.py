class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        
        for val,cunt in d.items():
            heapq.heappush(heap,(cunt,val))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []
        for cunt,val in heap:
            ans.append(val)
        return ans