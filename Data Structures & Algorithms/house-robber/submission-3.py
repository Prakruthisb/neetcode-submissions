class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n+1)
        dp[0] = nums[0]

        for i in range(1,n):
            pick = nums[i]
            if i>1:
                pick += dp[i-2]
            not_pick = dp[i-1]
            dp[i] = max(pick,not_pick)
        
        return dp[n-1]