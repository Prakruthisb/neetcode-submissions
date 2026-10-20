import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        for i in range(n):
            ans.append(math.prod(nums[0:i]) * math.prod(nums[i+1:n]))

        return ans