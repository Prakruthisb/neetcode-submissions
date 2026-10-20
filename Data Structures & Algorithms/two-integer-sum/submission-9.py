class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i,num in enumerate(nums):
            a.append((num,i))
        a.sort(key=lambda x:x[0])
        n = len(a)
        i,j = 0,n-1
        while i<j:
            summ = a[i][0] + a[j][0]
            if summ == target:
                return [min(a[i][1],a[j][1]),max(a[i][1],a[j][1])]
            elif summ > target:
                j-=1 
            else:
                i+=1       