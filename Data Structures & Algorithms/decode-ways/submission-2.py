class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)

        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            sub = s[i:]
            if dp[i] != 0:
                return dp[i]
            if sub[0] == '0':
                return 0
            # if 1 <= int(sub) <= 9:
            #     # happy base case
            #     return 1
            # if 1 <= int(sub) <= 26:
            #     return 1
            
            small = dfs(i + 1) if i + 1 <= len(s) and 1 <= int(s[i:i+1]) <= 26 else 0
            big = dfs(i + 2) if i + 2 <= len(s) and 1 <= int(s[i:i+2]) <= 26 else 0
            ways = small + big

            dp[i] = ways

            return ways
        
        return dfs(0)

