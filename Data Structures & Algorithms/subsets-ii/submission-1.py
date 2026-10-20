class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        
        def fun(i,arr):
            if i>=n:
                ans.add(tuple(arr.copy()))
                return
            arr.append(nums[i])
            fun(i+1,arr)

            arr.pop()
            fun(i+1,arr)
        
        fun(0,[])
        return [list(i) for i in ans]