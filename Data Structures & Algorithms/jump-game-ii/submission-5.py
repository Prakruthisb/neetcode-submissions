class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        jump = 0
        while True:
            if r >= (n-1):
                return jump
            temp = r
            r = max(l+nums[l],r+nums[r]) 
            l = temp+1
            jump += 1