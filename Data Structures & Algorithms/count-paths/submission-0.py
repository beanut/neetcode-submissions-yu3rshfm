class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # height = m
        # width = n
        # Bottom-Up (Tabulation) DP

        count = 0

        dp = [[0] * n for _ in range(m)]

        for ni in range(n):
            dp[m - 1][ni] = 1
        
        for mi in range(m):
            dp[mi][n - 1] = 1
        
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[r][c] = dp[r + 1][c] + dp[r][c + 1]
        
        return dp[0][0]