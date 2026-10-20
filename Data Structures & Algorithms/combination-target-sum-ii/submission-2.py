class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []

        def fun(start,arr,t):
            if t == 0:
                ans.append(arr.copy())
                return 

            for i in range(start,n):
                
                if i>start and candidates[i] == candidates[i-1]:
                    continue 

                if candidates[i] > t:
                    break 

                arr.append(candidates[i])
                fun(i+1,arr,t-candidates[i]) 

                arr.pop()
        
        fun(0,[],target) 

        return ans