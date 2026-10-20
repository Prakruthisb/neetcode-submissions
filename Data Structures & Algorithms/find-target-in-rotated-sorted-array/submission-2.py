class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = -1
        n = len(nums)
        l,r = 0,n-1
        ans = -1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] < nums[mid-1]:
                pivot = mid
                break
            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        
        left_half = nums[:pivot]
        right_half = nums[pivot:]

        ll,lr = 0,len(left_half)-1
        while ll <= lr:
            mid = (ll+lr)//2
            if left_half[mid] == target:
                ans = mid 
                break
            elif left_half[mid] > target:
                lr = mid -1 
            else:
                ll = mid + 1
        
        rl,rr = 0,len(right_half)-1
        while rl <= rr:
            mid = (rl+rr)//2
            if right_half[mid] == target:
                ans = len(left_half) + mid 
                break
            elif right_half[mid] > target:
                rr = mid -1 
            else:
                rl = mid + 1
        return ans