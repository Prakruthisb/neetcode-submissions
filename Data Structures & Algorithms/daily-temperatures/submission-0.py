class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n

        for i in range(n):
            cunt = 0
            flag = False
            for j in range(i,n):
                if temperatures[j] > temperatures[i]:
                    flag = True 
                    break 
                else:
                    cunt += 1 
            if flag:
                ans[i] = cunt
        return ans