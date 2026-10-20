class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+2)
        dp[n],dp[n+1] = 0,0

        for i in range(n-1,-1,-1):
            p = nums[i]+dp[i+2]
            n_p = dp[i+1]
            dp[i] = max(p,n_p)
        
        return dp[0]