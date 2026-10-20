class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        def fun(i,arr):
            if i>=n:
                ans.append(arr.copy())
                return
            arr.append(nums[i])
            fun(i+1,arr)

            arr.pop()
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1
            fun(i+1,arr)
        
        fun(0,[])
        return ans