class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = -1
        n = len(nums)
        l,r = 0,n-1

        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
        pivot = l

        def binary_search(l,r):
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid -1 
                else:
                    l = mid + 1
            return -1
        
        if target >= nums[pivot] and target <= nums[n-1]:
            return binary_search(pivot,n-1)
        else:
            return binary_search(0,pivot-1)
        
        