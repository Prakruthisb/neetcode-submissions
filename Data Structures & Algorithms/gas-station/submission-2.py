class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1 
        
        n = len(gas) 

        diff = [gas[i] - cost[i] for i in range(n)]
        
        total = 0 
        st_ind = 0

        for i in range(n):
            total += diff[i]
            if total < 0:
                total = 0 
                st_ind = i+1
        
        return st_ind