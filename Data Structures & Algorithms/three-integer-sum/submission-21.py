class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            if i>0 and i<n and nums[i] == nums[i-1]:
                continue
            h = set()
            for j in range(i+1,n):
                target = -(nums[i]+nums[j])
                if target in h:
                    ans.add((nums[i],target,nums[j]))
                h.add(nums[j])
        return [list(t) for t in ans]