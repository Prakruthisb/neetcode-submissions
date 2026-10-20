import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        
        pre = [0]*n
        suf = [0]*n

        pre[0],suf[n-1] = 1,1

        pre_mul = nums[0]
        for i in range(1,n):
            pre[i] = pre_mul 
            pre_mul *= nums[i]
        
        suf_mul = nums[n-1]
        for i in range(n-2,-1,-1):
            suf[i] = suf_mul
            suf_mul *= nums[i]

        for i in range(n):
            ans[i] = pre[i]*suf[i]

        return ans