class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        dup = set()
        for i in range(n):
            if i and nums[i] == nums[i-1]:
                continue 
            h = set()
            for j in range(i+1,n):
                target = -(nums[i]+nums[j])
                if target in h:
                    triplet = (nums[i],target,nums[j])
                    if triplet not in dup:
                        ans.append(list(triplet))
                        dup.add(triplet)
                h.add(nums[j])
        return ans