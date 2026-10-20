class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*n

        def f(i):
            if i >= (n-1):
                return 0
            if dp[i] != float('inf'):
                return dp[i]
            for j in range(1,nums[i]+1):
                if i+j < n:
                    dp[i] = min(dp[i],1+f(i+j))
            return dp[i]
        
        return f(0)