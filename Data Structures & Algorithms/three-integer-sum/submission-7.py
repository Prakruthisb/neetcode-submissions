class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i and nums[i] == nums[i-1]:
                continue 
            l,r = i+1,n-1
            while l<r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if r > n-1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                summ = nums[i]+nums[l]+nums[r]
                if summ == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l += 1 
                    r -= 1 
                elif summ > 0:
                    r -= 1
                elif summ < 0:
                    l += 1 
        return ans