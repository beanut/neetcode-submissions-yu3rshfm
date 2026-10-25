class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[-1] * len(word1) for _ in range(len(word2))]

        def dfs(i, j) -> int:
            if i < 0:
                return j + 1 # insertions
            if j < 0:
                return i + 1 # deletions
            if dp[j][i] > -1:
                return dp[j][i]
            
            if word1[i] == word2[j]:
                dp[j][i] = dfs(i - 1, j - 1)
            else:
                dp[j][i] = 1 + min(
                    dfs(i, j - 1),  # insert
                    dfs(i - 1, j),   # delete
                    dfs(i - 1, j - 1)   # replace
                )
            
            return dp[j][i]

        return dfs(len(word1) - 1, len(word2) - 1)