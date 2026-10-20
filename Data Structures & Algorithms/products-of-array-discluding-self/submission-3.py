import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        n_zeros = 0
        for num in nums:
            if num == 0:
                n_zeros += 1 

        product = 1
        ind = -1

        for i in range(n):
            if nums[i] != 0:
                product *= nums[i] 
                ans[i] = 0
            else:
                ind = i

        if n_zeros > 1:
             return ans 
        elif n_zeros == 1:
            ans[ind] = product 
        else:
            for i in range(n):
                ans[i] = product//nums[i]
        return ans
                