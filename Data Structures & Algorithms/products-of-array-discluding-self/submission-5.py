import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n

        pre,suf = 1,1
        for i in range(n):
            ans[i] = pre
            pre *= nums[i]
        
        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * suf
            suf *= nums[i]

        return ans