class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = 0
        for i in range(n-1):
            ans = max(nums[i]+i,ans)
            if (ans == i and nums[i] == 0) or (ans >= n-1):
                break
        if ans >= n-1:
            return True
        return False