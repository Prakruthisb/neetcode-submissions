class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        def fun(ind,target):
            if ind == 0:
                if target % coins[ind] == 0:
                    return target//coins[ind] 
                else:
                    return float('inf')
            
            not_pick = fun(ind-1,target)

            pick = float('inf')
            if coins[ind] <= target:
                pick = 1 + fun(ind,target-coins[ind])

            return min(not_pick,pick)
        
        ans = fun(n-1,amount)
        return -1 if ans == float('inf') else ans