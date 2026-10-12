class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [None] * (len(s) + 1)

        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            if dp[i] is not None:
                return dp[i]
            if s[i] == '0':
                return 0
            
            small = dfs(i + 1) if i + 1 <= len(s) and 1 <= int(s[i:i+1]) <= 26 else 0
            big = dfs(i + 2) if i + 2 <= len(s) and 1 <= int(s[i:i+2]) <= 26 else 0
            ways = small + big

            dp[i] = ways

            return ways
        
        return dfs(0)

