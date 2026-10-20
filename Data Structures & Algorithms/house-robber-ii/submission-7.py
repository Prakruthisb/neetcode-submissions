class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]
        
        def fun(s,e,dp):
            if s>=e:
                return 0 
            if dp[s] != -1:
                return dp[s]
            p = nums[s] + fun(s+2,e,dp)
            n_p = fun(s+1,e,dp)
            dp[s] = max(p,n_p)
            return dp[s]
        
        ans1 = fun(0,n-1,[-1]*n)
        ans2 = fun(1,n,[-1]*n)
        return max(ans1,ans2)