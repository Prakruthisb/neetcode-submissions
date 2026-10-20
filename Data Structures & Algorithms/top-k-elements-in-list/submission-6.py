class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num,0)+1
        
        arr = [[] for _ in range(len(nums)+1)] 

        for val,cunt in d.items():
            arr[cunt].append(val) 
        
        ans = []
        for i in range(len(arr)-1,0,-1):
            for val in arr[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans 