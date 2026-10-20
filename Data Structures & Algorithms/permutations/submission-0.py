class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) 
        ans = []

        def fun(visited,arr):
            if len(arr) == n:
                ans.append(arr.copy())
                return 
            
            for i in range(len(nums)):
                if not visited[i]:
                    arr.append(nums[i])
                    visited[i] = 1 
                    fun(visited,arr)
                    visited[i] = 0 
                    arr.pop()
        
        visited = [0] * n
        fun(visited,[])
        return ans 