class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        ans = [1]*n

        for i in range(1,n):
            ans[i] = nums[i-1]*prefix
            prefix = ans[i]
        
        for i in range(n-2,-1,-1):
            ans[i] *= nums[i+1]*suffix
            suffix = nums[i+1]*suffix
        
        return ans
