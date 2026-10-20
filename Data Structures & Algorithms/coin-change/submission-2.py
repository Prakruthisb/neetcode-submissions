class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = float('inf')
        dp = [[INF]*(amount+1) for _ in range(n)]

        for target in range(amount+1):
            if target % coins[0] == 0:
                dp[0][target] = target//coins[0] 

        for i in range(1,n):
            for target in range(amount+1):

                not_pick = dp[i-1][target]

                pick = INF
                if coins[i] <= target:
                    pick = 1 + dp[i][target-coins[i]]

                dp[i][target] = min(not_pick,pick)
        
        ans = dp[-1][amount]
        return -1 if ans == INF else ans