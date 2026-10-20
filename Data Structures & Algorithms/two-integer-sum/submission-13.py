class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        d = {}
        for i,val in enumerate(nums):
            req = target-val
            if req in d:
                return [d[req],i]
            else:
                d[val] = i