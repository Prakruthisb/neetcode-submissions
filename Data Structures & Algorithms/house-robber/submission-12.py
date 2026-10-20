class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        p1,p2 = 0,0

        for i in range(n-1,-1,-1):
            temp = max(nums[i]+p2,p1)
            p2 = p1
            p1 = temp 
        
        return max(p1,p2)