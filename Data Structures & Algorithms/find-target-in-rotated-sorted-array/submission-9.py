class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i,j = 0,n-1

        def bs(i,j):
            while i<=j:
                m = (i+j)//2 
                if nums[m] == target:
                    return m 
                elif nums[m] > target:
                    j = m-1
                else:
                    i = m+1
            return -1

        #find pivot
        while i<j:
            m = (i+j)//2 
            if nums[m] > nums[j]:
                i = m+1
            else:
                j = m 
        
        if nums[i] <= target <= nums[n-1]:
            index = bs(i,n-1)
        else:
            index = bs(0,i-1)
        return index 
