class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)

        def fun(index,arr,summ):
            if summ == target:
                ans.append(arr.copy())
                return 
            elif summ > target or index>=n:
                return 
            arr.append(nums[index])
            fun(index,arr,summ+nums[index])

            arr.pop()
            fun(index+1,arr,summ)
        
        fun(0,[],0)
        return ans