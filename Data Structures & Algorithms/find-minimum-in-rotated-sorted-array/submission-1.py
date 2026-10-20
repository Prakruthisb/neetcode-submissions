class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        i,j = 0,n-1
        while i<j:
            m = (i+j)//2
            if nums[m] > nums[j]:
                i = m+1
            else:
                j = m
        return nums[i]