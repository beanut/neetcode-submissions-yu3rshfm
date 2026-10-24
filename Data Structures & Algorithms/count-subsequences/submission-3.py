class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

        for c in range(len(s) + 1):
            dp[len(t)][c] = 1
        
        for r in range(len(t) - 1, -1, -1):
            for c in range(len(s) - 1, -1, -1):
                if s[c] == t[r]:
                    dp[r][c] = dp[r + 1][c + 1] + dp[r][c + 1]
                else:
                    dp[r][c] = dp[r][c + 1]

        return dp[0][0]
