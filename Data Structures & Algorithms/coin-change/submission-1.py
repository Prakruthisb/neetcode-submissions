class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]

        def fun(ind,target):
            if ind == 0:
                if target % coins[ind] == 0:
                    return target//coins[ind] 
                else:
                    return float('inf')

            if dp[ind][target] != -1:
                return dp[ind][target]

            not_pick = fun(ind-1,target)

            pick = float('inf')
            if coins[ind] <= target:
                pick = 1 + fun(ind,target-coins[ind])

            dp[ind][target] = min(not_pick,pick)
            return dp[ind][target]
        
        ans = fun(n-1,amount)
        return -1 if ans == float('inf') else ans