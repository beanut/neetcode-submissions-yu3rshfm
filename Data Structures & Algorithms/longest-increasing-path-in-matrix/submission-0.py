class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        COLS = len(matrix[0])
        ROWS = len(matrix)
        dp = [[-1] * COLS for _ in range(ROWS)]
        longest = 0

        def dfs(r, c, last) -> int:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return 0

            cur = matrix[r][c]
            if not cur > last:
                return 0

            if dp[r][c] > -1:
                return dp[r][c]
            
            dp[r][c] = 1 + max(
                dfs(r + 1, c, cur),
                dfs(r - 1, c, cur),
                dfs(r, c + 1, cur),
                dfs(r, c - 1, cur)
            )

            return dp[r][c]

        return max(
            dfs(r, c, float("-inf"))
            for r in range(ROWS)
            for c in range(COLS)
        )
            