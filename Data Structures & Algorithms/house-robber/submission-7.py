class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*(n)

        def fun(index):
            if index < 0:
                return 0
            if dp[index] != -1:
                return dp[index]
            pick = nums[index]+fun(index-2)
            not_pick = 0 + fun(index-1)
            dp[index] = max(pick,not_pick)
            return dp[index]
        
        return fun(n-1)