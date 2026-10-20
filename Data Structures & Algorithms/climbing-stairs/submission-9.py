class Solution:
    def climbStairs(self, n: int) -> int:
        p1,p2 = 0,1
        for i in range(1,n+1):
            temp = p2 
            p2 = p1+p2
            p1 = temp 
        return p2