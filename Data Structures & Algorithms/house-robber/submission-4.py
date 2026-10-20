class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        p1 = nums[0]
        p2 = 0

        for i in range(1,n):
            pick = nums[i]
            if i>1:
                pick += p2
            not_pick = p1
            cur = max(pick,not_pick)
            p2 = p1 
            p1 = cur 
        
        return p1