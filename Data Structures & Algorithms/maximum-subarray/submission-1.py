class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')

        s = 0 
        for num in nums:
            s += num 
            ans = max(ans,s)
            if s < 0:
                s = 0 
        
        return ans 