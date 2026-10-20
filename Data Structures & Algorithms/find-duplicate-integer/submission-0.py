class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = defaultdict(int)

        for num in nums:
            d[num] = d.get(num,0)+1
        
        for k,v in d.items():
            if v >=2 :
                return k