class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0,n-1

        def fun(l,r):
            if l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid 
                elif nums[mid] > target:
                    return fun(l,mid-1)
                else:
                    return fun(mid+1,r)
            else:
                return -1
        
        ans = fun(l,r)
        return ans