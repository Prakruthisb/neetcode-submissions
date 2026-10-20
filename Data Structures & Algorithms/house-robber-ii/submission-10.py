class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]

        p1,p2 = 0,0

        for i in range(n-2,-1,-1):
            temp = max(p1,nums[i]+p2)
            p2 = p1
            p1 = temp
        
        ans = p1
        
        p1,p2 = 0,0 

        for i in range(n-1,0,-1):
            temp = max(p1,nums[i]+p2)
            p2 = p1
            p1 = temp

        return max(ans,p1)