class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = []

        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                top = stack.pop()
                ans[top[1]] = i-top[1]
            stack.append((temperatures[i],i)) 
        return ans