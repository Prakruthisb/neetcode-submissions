class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        def fun(i,arr):
            if i>=n:
                ans.append(arr.copy())
                return 
            
            arr.append(nums[i])
            fun(i+1,arr)
            arr.pop()
            fun(i+1,arr)
        
        fun(0,[])
        return ans 