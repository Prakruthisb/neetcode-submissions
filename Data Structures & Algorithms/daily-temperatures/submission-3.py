class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n

        s = []
        for i,val in enumerate(temperatures):
            while s and val > s[-1][0]:
                top = s.pop()
                result[top[1]] = i-top[1]
            s.append((val,i))
        return result 
