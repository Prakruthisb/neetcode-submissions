class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        if sum(nums) % 2 != 0:
            return False

        def f(ind,s,t):
            if s==t:
                return True 
            if s>t or ind>=n:
                return False 
            if f(ind+1,s+nums[ind],t):
                return True 
            if f(ind+1,s,t):
                return True 
            return False
        
        return f(0,0,sum(nums)//2)