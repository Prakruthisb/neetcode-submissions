class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums) 
        curMax,curMin = 1,1

        for n in nums:
            if n==0:
                curMax,curMin = 1,1
                continue 

            temp = n*curMax
            curMax = max(n,n*curMax,n*curMin)
            curMin = min(n,temp,n*curMin)

            ans = max(ans,curMax)
        
        return ans 