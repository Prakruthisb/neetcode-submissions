class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        p1,p2 = 0,0 

        for i in range(n-1,-1,-1):
            temp = p1 
            p1 = cost[i] + min(p1,p2)
            p2 = temp 

        return min(p1,p2)