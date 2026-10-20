class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = float('inf')
        prev = [INF]*(amount+1)

        for target in range(amount+1):
            if target % coins[0] == 0:
                prev[target] = target//coins[0] 

        for i in range(1,n):
            cur = [INF]*(amount+1)
            for target in range(amount+1):

                not_pick = prev[target]

                pick = INF
                if coins[i] <= target:
                    pick = 1 + cur[target-coins[i]]

                cur[target] = min(not_pick,pick)
            prev = cur
        
        ans = prev[amount]
        return -1 if ans == INF else ans