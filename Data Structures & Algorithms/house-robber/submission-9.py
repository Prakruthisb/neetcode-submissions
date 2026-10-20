class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n

        def fun(ind):
            if ind>=n:
                return 0 
            if dp[ind] != -1:
                return dp[ind]
            p = nums[ind]+fun(ind+2)
            n_p = fun(ind+1)
            dp[ind] = max(p,n_p)
            return dp[ind]
        
        return fun(0)