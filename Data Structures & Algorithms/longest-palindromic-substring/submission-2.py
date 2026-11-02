class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        resstart, resend = 0, 0

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            # check palindromicity
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i > resend - resstart:
                        resstart, resend = i, j

        return s[resstart:resend+1]