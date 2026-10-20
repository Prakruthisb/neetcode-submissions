class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i,j = 0,n-1

        while i<=j:
            m = (i+j)//2
            if nums[m] == target:
                return m 
            elif nums[m] > target:
                j = m -1 
            else:
                i = m + 1 
        return -1