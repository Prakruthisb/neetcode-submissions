import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n):
            mul = 1
            for j in range(0,i):
                mul *= nums[j] 

            for j in range(i+1,n):
                mul *= nums[j]

            ans.append(mul)

        return ans