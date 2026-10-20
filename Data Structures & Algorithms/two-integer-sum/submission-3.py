class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i,num in enumerate(nums):
            A.append((num,i))
        A.sort(key=lambda x:x[0])
        n = len(nums)
        i,j = 0,n-1
        while i < j:
            summ = A[i][0] + A[j][0]
            if summ == target:
                return [min(A[i][1],A[j][1]),
                        max(A[i][1],A[j][1])]
            elif summ > target:
                j -= 1 
            else:
                i += 1 
            