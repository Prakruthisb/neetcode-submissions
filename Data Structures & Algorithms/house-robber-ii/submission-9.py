class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]

        dp1 = [-1]*(n+1)
        dp1[n-1],dp1[n] = 0,0

        for i in range(n-2,-1,-1):
            p = nums[i] + dp1[i+2]
            n_p = dp1[i+1]
            dp1[i] = max(p,n_p)
        
        dp2 = [-1]*(n+2)
        dp2[n],dp2[n+1] = 0,0 

        for i in range(n-1,0,-1):
            p = nums[i] + dp2[i+2]
            n_p = dp2[i+1]
            dp2[i] = max(p,n_p)

        return max(dp1[0],dp2[1])