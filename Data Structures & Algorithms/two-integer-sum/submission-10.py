class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            req = target - nums[i]
            if req in h:
                return [min(h[req],i),max(h[req],i)]
            else:
                h[nums[i]] = i