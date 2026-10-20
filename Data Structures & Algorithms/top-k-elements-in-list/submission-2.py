class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        heap = []

        for num in nums:
            d[num] = d.get(num,0)+1
        
        for v,f in d.items():
            heapq.heappush(heap,(f,v))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [i[1] for i in heap]