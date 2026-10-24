class Solution:
    # Oct 24: Tool 6 mins to solve lmao
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        
        def dfs(r: int, start: int) -> int:
            if r < 0:
                return 0
            if r == 0:
                return 1
            if dp[start][r] > -1:
                return dp[start][r]

            curTotal = 0
            
            for idx in range(start, len(coins)):
                curTotal += dfs(r - coins[idx], idx)
            
            dp[start][r] = curTotal

            return curTotal

        return dfs(amount, 0)
